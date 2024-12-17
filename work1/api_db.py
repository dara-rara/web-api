import asyncio
import json
from fastapi import FastAPI, Depends, HTTPException, WebSocket
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from starlette.websockets import WebSocketDisconnect
from starlette.concurrency import run_in_threadpool
from sqlmodel import SQLModel, Field

from parser2 import parse_maxidom


class Prices(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    price: int


class MessageWB:
    @staticmethod
    def message(msg: str) -> str:
        return json.dumps({"message": msg})


class ConnectionManagerWS:
    def __init__(self):
        self.connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    async def broadcast(self, data: str):
        for conn in self.connections:
            await conn.send_text(data)


def get_async_session():
    sqlite_url = "sqlite+aiosqlite:///parser.db"
    engine = create_async_engine(sqlite_url)
    dbsession = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    return dbsession()


async def get_session():
    async with get_async_session() as session:
        yield session


app = FastAPI()
SessionDep = Depends(get_session)
manager = ConnectionManagerWS()


async def init_models(engine):
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def create_db_and_tables():
    sqlite_url = "sqlite+aiosqlite:///parser.db"
    engine = create_async_engine(sqlite_url)
    await init_models(engine)


async def background_parser_async(session: AsyncSession):
    while True:
        await asyncio.sleep(60 * 60 * 12)
        print("Starting get price")
        await background_add_item(session)
        await manager.broadcast(MessageWB.message("Update database"))


async def background_add_item(session: AsyncSession):
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
async def startup_event():
    await create_db_and_tables()
    asyncio.create_task(background_parser_async(get_async_session()))


@app.get("/start_parser")
async def start_parser():
    asyncio.create_task(background_add_item(get_async_session()))
    return {"status": "data create"}


@app.get("/prices")
async def read_prices(session: AsyncSession = SessionDep, offset: int = 0, limit: int = 10):
    data = await session.scalars(select(Prices).offset(offset).limit(limit))
    return data.all()


@app.get("/prices/{item_id}")
async def read_item(item_id: int, session: AsyncSession = SessionDep):
    price = await session.get(Prices, item_id)
    if not price:
        raise HTTPException(status_code=404, detail="Price not found")
    return price


@app.put("/prices/{item_id}")
async def update_item(item_id: int, data: Prices, session: AsyncSession = SessionDep):
    price_db = await session.get(Prices, item_id)
    if not price_db:
        raise HTTPException(status_code=404, detail="Price not found")
    price_data = data.model_dump(exclude_unset=True)
    price_db.sqlmodel_update(price_data)
    session.add(price_db)
    await session.commit()
    await session.refresh(price_db)
    await manager.broadcast(MessageWB.message(f"Update item {item_id}"))
    return price_db


@app.post("/prices/create")
async def create_item(item: Prices, session: AsyncSession = SessionDep):
    session.add(item)
    await session.commit()
    await session.refresh(item)
    await manager.broadcast(MessageWB.message(f"Create item {item.id}"))
    return item


@app.delete("/prices/{item_id}")
async def delete_item(item_id: int, session: AsyncSession = SessionDep):
    price = await session.get(Prices, item_id)
    if not price:
        raise HTTPException(status_code=404, detail="Price not found")
    await session.delete(price)
    await session.commit()
    await manager.broadcast(MessageWB.message(f"Delete item {item_id}"))
    return {"status": "item delete"}


@app.websocket("/ws")
async def ws_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(data)
    except WebSocketDisconnect:
        print(f"Client {websocket} disconnect")


#fastapi dev api_db.py