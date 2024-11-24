import asyncio
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from parser2 import parse_maxidom
from starlette.concurrency import run_in_threadpool
from sqlmodel import Field, SQLModel, create_engine, Session, select


class Prices(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    price: int


def get_async_session():
    sqlite_url = "sqlite+aiosqlite:///parser.db"
    engine = create_async_engine(sqlite_url)
    dbsession = async_sessionmaker(engine)
    return dbsession()


async def get_session():
    async with get_async_session() as session:
        yield session


app = FastAPI()
SessionDep = Depends(get_session)


def create_db_and_tables():
    SQLModel.metadata.create_all(create_engine("sqlite:///parser.db"))


async def background_parser_async(session: Session):
    while True:
        print("Starting get price")
        await asyncio.sleep(12 * 60 * 60)
        await background_add_item(session)


async def background_add_item(session: Session):
    data = await run_in_threadpool(parse_maxidom)
    for item in data:
        existing_item = await session.execute(select(Prices).where(Prices.title == item['title']))
        existing_item = existing_item.scalar_one_or_none()
        if existing_item:
            existing_item.price = item['price']
        else:
            new_item = Prices(title=item['title'], price=item['price'])
            session.add(new_item)
    await session.commit()


@app.on_event("startup")
async def startup_event(session: Session = SessionDep):
    create_db_and_tables()
    asyncio.create_task(background_parser_async(session))


@app.get("/start_parser")
async def start_parser(session: Session = SessionDep):
    asyncio.create_task(background_add_item(session))
    return {"status": "data create"}


@app.get("/prices")
async def read_prices(session: Session = SessionDep, offset: int = 0, limit: int = 10):
    data = await session.scalars(select(Prices).offset(offset).limit(limit))
    return data.all()


@app.get("/prices/{item_id}")
async def read_item(item_id: int, session: Session = SessionDep):
    price = await session.get(Prices, item_id)
    if not price:
        raise HTTPException(status_code=404, detail="Price not found")
    return price


@app.put("/prices/{item_id}")
async def update_item(item_id: int, data: Prices, session: Session = SessionDep):
    price_db = await session.get(Prices, item_id)
    if not price_db:
        raise HTTPException(status_code=404, detail="Price not found")
    price_data = data.model_dump(exclude_unset=True)
    price_db.sqlmodel_update(price_data)
    session.add(price_db)
    await session.commit()
    await session.refresh(price_db)
    return price_db


@app.post("/prices/create")
async def create_item(item: Prices, session: Session = SessionDep):
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item


@app.delete("/prices/{item_id}")
async def delete_item(item_id: int, session: Session = SessionDep):
    price = await session.get(Prices, item_id)
    if not price:
        raise HTTPException(status_code=404, detail="Price not found")
    await session.delete(price)
    await session.commit()
    return {"status": "item delete"}