import requests as rq
from bs4 import BeautifulSoup
from selenium import webdriver

# response = rq.get(url='https://e1.ru')
# soup = BeautifulSoup(response.content, 'lxml')
# traffic = soup.find('span', class_='level_3XueO green_3XueO text-style-ui-menu-bold')
# print(traffic.text)

# response = rq.get(url='https://www.maxidom.ru/catalog/dushevye-sistemy/1001529332/')
# soup = BeautifulSoup(response.content, 'lxml')
# title = soup.find('span', itemprop='name')
# print(title.text)

# response = rq.get(url='https://www.maxidom.ru/catalog/dushevye-sistemy/1001529332/')
# soup = BeautifulSoup(response.content, 'lxml')
# price = soup.find('div', class_='lvl1__product-body-buy-price-base')
# print(price['data-repid_price'])


# response = rq.get(
#     url="https://www.sdvor.com/ekb/product/gruntovka-ceresit-ct17-10-l-11030"
# )
# soup = BeautifulSoup(response.content, "lxml")
#
# #  title = soup.find("cx-page-layout", class_="ProductDetailsPageTemplate")
# #  print(title.h1.get_text())
#
# #  def title_find(tag):
# #      #  return tag.has_attr("_ngcontent-sdvor-app-c3803368145")
# #      for attr in tag.attrs:
# #          if attr.startswith("_ngcontent-sdvor-app-"):
# #              return True
# #      return False
#
# title = soup.find(lambda tag: tag.has_attr("_ngcontent-sdvor-app-c3803368145"))
# print(title.get_text())

# response = rq.get(
#     url="https://www.sdvor.com/ekb/product/gruntovka-ceresit-ct17-10-l-11030"
# )
# soup = BeautifulSoup(response.content, "lxml")
#
# title = soup.find(lambda tag: tag.has_attr("_ngcontent-sdvor-app-c3803368145"))
# print(title.get_text())
#
# price = soup.find("div", class_="price").span.text
# print(price)
# print(int("".join(filter(str.isdigit, price))))
#
# cookies = {
#     'cf_clearance': 'T_SsKswFZJQu3OSW36UHCAARruH1OL5p74am0t6uRcM-1709468935-1.0.1.1-NSnAC0upL7geVy5TYs87JaMuLLAVRp3H.tSKtvYLPo1xbMuWmDUttqAF_0lIoHF9UhIOsLkm3U3MC5TEaaB0LA',
#     'abt_data': 'b2dc299ba0f1611460974787e5ad2256:adf56849ab6da912e952a6b7ca64e33cb459c6508d338f817f2f7b6a2290b46b61a8c63300cda5d062b75f134d9142f05d7d814725931d75ce20c86b0c93231b7b18ecf33f963dc2e22f622fbfd543ae2d235fb14eb6ce26b11616d0e90bc06b92a5bccfa57c8f72bfae5fc96040af5e566f260c01fd35b1d475ed6015dc069597bcfd45bd52eea8d1bca59ddf188e3031c1fb26d5a1ac047abd72c4eaaf03a873f5b1d569bd0d813f555a6f844de909d1f3d4869a9d7579d552755490793f680d3d045161431562af959ef0e266272c2900d613b300909d3c64256083295442dbdabe11fc1dd378e1dd36d2327a75870e5f2a944919b7d41a85068f142e7b10694e438a5e7785504e4df020c84a3f5cfe714358008d484186b9d9dfcc5a8aa003bf53563c1d38a611322a5eebeb284364351aec7799a53228c6537118dfc71ee8df3d1c613655be2ff5b0816f10936b2e0bf7ff22fa181e234f013bb9e08e2a',
#     '__Secure-ab-group': '15',
#     '__Secure-user-id': '0',
#     '__Secure-ext_xcid': '32d04a373fb90ac7bd12fb40c1a47487',
#     '__Secure-ETC': 'e33b1ee2e07a7eb9dbee78f0e815a4d2',
#     '__Secure-access-token': '6.0.GuDAcRAbTpKm-Kq01tp1SA.15.AU8hUyPJIg_EmjnjcbXIif70QuIOcHBeeRHQvEummuDcyFzV5HEgInsUe1U_zk_4kQ..20241020230016.mX9J0eMi1k40WUy7QXuJk5Xb1uPnOXy0vyDsZ2TDuNY.15bdae801c1bfecde',
#     '__Secure-refresh-token': '6.0.GuDAcRAbTpKm-Kq01tp1SA.15.AU8hUyPJIg_EmjnjcbXIif70QuIOcHBeeRHQvEummuDcyFzV5HEgInsUe1U_zk_4kQ..20241020230016.oszjOtDwcfGVdax-c6jGUWrynJrOXZ9CdL9GKHg8LNE.17bbd662083e143a2',
#     'xcid': '0345ecf154ab53275719dd743130e95f',
#     'rfuid': 'NjkyNDcyNDUyLDEyNC4wNDM0NzUyNzUxNjA3NCwtMTEyOTg2MTc1NywtMSwtMjIzMzcwNzE0LFczc2libUZ0WlNJNklsQkVSaUJXYVdWM1pYSWlMQ0prWlhOamNtbHdkR2x2YmlJNklsQnZjblJoWW14bElFUnZZM1Z0Wlc1MElFWnZjbTFoZENJc0ltMXBiV1ZVZVhCbGN5STZXM3NpZEhsd1pTSTZJbUZ3Y0d4cFkyRjBhVzl1TDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMHNleUowZVhCbElqb2lkR1Y0ZEM5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlYWDBzZXlKdVlXMWxJam9pUTJoeWIyMWxJRkJFUmlCV2FXVjNaWElpTENKa1pYTmpjbWx3ZEdsdmJpSTZJbEJ2Y25SaFlteGxJRVJ2WTNWdFpXNTBJRVp2Y20xaGRDSXNJbTFwYldWVWVYQmxjeUk2VzNzaWRIbHdaU0k2SW1Gd2NHeHBZMkYwYVc5dUwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjBzZXlKMGVYQmxJam9pZEdWNGRDOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5WFgwc2V5SnVZVzFsSWpvaVEyaHliMjFwZFcwZ1VFUkdJRlpwWlhkbGNpSXNJbVJsYzJOeWFYQjBhVzl1SWpvaVVHOXlkR0ZpYkdVZ1JHOWpkVzFsYm5RZ1JtOXliV0YwSWl3aWJXbHRaVlI1Y0dWeklqcGJleUowZVhCbElqb2lZWEJ3YkdsallYUnBiMjR2Y0dSbUlpd2ljM1ZtWm1sNFpYTWlPaUp3WkdZaWZTeDdJblI1Y0dVaU9pSjBaWGgwTDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMWRmU3g3SW01aGJXVWlPaUpOYVdOeWIzTnZablFnUldSblpTQlFSRVlnVm1sbGQyVnlJaXdpWkdWelkzSnBjSFJwYjI0aU9pSlFiM0owWVdKc1pTQkViMk4xYldWdWRDQkdiM0p0WVhRaUxDSnRhVzFsVkhsd1pYTWlPbHQ3SW5SNWNHVWlPaUpoY0hCc2FXTmhkR2x2Ymk5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlMSHNpZEhsd1pTSTZJblJsZUhRdmNHUm1JaXdpYzNWbVptbDRaWE1pT2lKd1pHWWlmVjE5TEhzaWJtRnRaU0k2SWxkbFlrdHBkQ0JpZFdsc2RDMXBiaUJRUkVZaUxDSmtaWE5qY21sd2RHbHZiaUk2SWxCdmNuUmhZbXhsSUVSdlkzVnRaVzUwSUVadmNtMWhkQ0lzSW0xcGJXVlVlWEJsY3lJNlczc2lkSGx3WlNJNkltRndjR3hwWTJGMGFXOXVMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4wc2V5SjBlWEJsSWpvaWRHVjRkQzl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOVhYMWQsV3lKeWRTMVNWU0pkLDAsMSwwLDI0LDIzNzQxNTkzMCw4LDIyNzEyNjUyMCwwLDEsMCwtNDkxMjc1NTIzLFIyOXZaMnhsSUVsdVl5NGdUbVYwYzJOaGNHVWdSMlZqYTI4Z1YybHVNeklnTlM0d0lDaFhhVzVrYjNkeklFNVVJREV3TGpBN0lGZHBialkwT3lCNE5qUXBJRUZ3Y0d4bFYyVmlTMmwwTHpVek55NHpOaUFvUzBoVVRVd3NJR3hwYTJVZ1IyVmphMjhwSUVOb2NtOXRaUzh4TWprdU1DNHdMakFnVTJGbVlYSnBMelV6Tnk0ek5pQXlNREF6TURFd055Qk5iM3BwYkd4aCxleUpqYUhKdmJXVWlPbnNpWVhCd0lqcDdJbWx6U1c1emRHRnNiR1ZrSWpwbVlXeHpaU3dpU1c1emRHRnNiRk4wWVhSbElqcDdJa1JKVTBGQ1RFVkVJam9pWkdsellXSnNaV1FpTENKSlRsTlVRVXhNUlVRaU9pSnBibk4wWVd4c1pXUWlMQ0pPVDFSZlNVNVRWRUZNVEVWRUlqb2libTkwWDJsdWMzUmhiR3hsWkNKOUxDSlNkVzV1YVc1blUzUmhkR1VpT25zaVEwRk9UazlVWDFKVlRpSTZJbU5oYm01dmRGOXlkVzRpTENKU1JVRkVXVjlVVDE5U1ZVNGlPaUp5WldGa2VWOTBiMTl5ZFc0aUxDSlNWVTVPU1U1SElqb2ljblZ1Ym1sdVp5SjlmWDE5LDY1LDUyMTA1MTkxMSwxLDEsLTEsMTY5OTk1NDg4NywxNjk5OTU0ODg3LC0yMDc1NjQwOTA3LDg=',
#     'abt_data': '7.pIfhIf1er7UWuBs9P3YEXVz6qUvoVhNKTdxTcxnkJxsGuMIwFOKzf0sNnAIxOfve465P46ShE0uKoxqovxDpIpZSDWmEVckkobIfgM4c8y-0b_urzRNIGTngXVrDKQjtHRnVFNuADYgLQ-kEU1x4bf3q8OY2Q3OJxp2G_Seh3YoVPoGYL2e3S9yLLysmKDDYwHUKkP-bP1miaCSNY5AAyMQbArATnHgi7Hf0VPsiCq6zq_ariub4uEDf_S71o3rKb28KFvvo3V1yGhR0fRpTppRmWIpNsLbQTGt3nIoRYDCxmjaEiO1UyF_VtKnwa-wWDi32-MWmott-JWx7b2ZxXqyWg4Gepg9DTGhF4wAiGXTgnxIrt0U3BlQB1F08PVD0plOO0UTDk8udAbiusdwt3XnpMcetZK9tSX8OgGm8hAC-IXVey0F8-ldohqmGiLOG_Hd4riGDDZHe65p-8oy_e8JJ9D6DkDbCxL4-9DC2KaNTXt9VoDXFBIpvJrFW9MQ7c_T4Kv5bFNrShaQyibY',
#     'ADDRESSBOOKBAR_WEB_CLARIFICATION': '1729458479',
# }
#
# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'cache-control': 'max-age=0',
#     # 'cookie': 'cf_clearance=T_SsKswFZJQu3OSW36UHCAARruH1OL5p74am0t6uRcM-1709468935-1.0.1.1-NSnAC0upL7geVy5TYs87JaMuLLAVRp3H.tSKtvYLPo1xbMuWmDUttqAF_0lIoHF9UhIOsLkm3U3MC5TEaaB0LA; abt_data=b2dc299ba0f1611460974787e5ad2256:adf56849ab6da912e952a6b7ca64e33cb459c6508d338f817f2f7b6a2290b46b61a8c63300cda5d062b75f134d9142f05d7d814725931d75ce20c86b0c93231b7b18ecf33f963dc2e22f622fbfd543ae2d235fb14eb6ce26b11616d0e90bc06b92a5bccfa57c8f72bfae5fc96040af5e566f260c01fd35b1d475ed6015dc069597bcfd45bd52eea8d1bca59ddf188e3031c1fb26d5a1ac047abd72c4eaaf03a873f5b1d569bd0d813f555a6f844de909d1f3d4869a9d7579d552755490793f680d3d045161431562af959ef0e266272c2900d613b300909d3c64256083295442dbdabe11fc1dd378e1dd36d2327a75870e5f2a944919b7d41a85068f142e7b10694e438a5e7785504e4df020c84a3f5cfe714358008d484186b9d9dfcc5a8aa003bf53563c1d38a611322a5eebeb284364351aec7799a53228c6537118dfc71ee8df3d1c613655be2ff5b0816f10936b2e0bf7ff22fa181e234f013bb9e08e2a; __Secure-ab-group=15; __Secure-user-id=0; __Secure-ext_xcid=32d04a373fb90ac7bd12fb40c1a47487; __Secure-ETC=e33b1ee2e07a7eb9dbee78f0e815a4d2; __Secure-access-token=6.0.GuDAcRAbTpKm-Kq01tp1SA.15.AU8hUyPJIg_EmjnjcbXIif70QuIOcHBeeRHQvEummuDcyFzV5HEgInsUe1U_zk_4kQ..20241020230016.mX9J0eMi1k40WUy7QXuJk5Xb1uPnOXy0vyDsZ2TDuNY.15bdae801c1bfecde; __Secure-refresh-token=6.0.GuDAcRAbTpKm-Kq01tp1SA.15.AU8hUyPJIg_EmjnjcbXIif70QuIOcHBeeRHQvEummuDcyFzV5HEgInsUe1U_zk_4kQ..20241020230016.oszjOtDwcfGVdax-c6jGUWrynJrOXZ9CdL9GKHg8LNE.17bbd662083e143a2; xcid=0345ecf154ab53275719dd743130e95f; rfuid=NjkyNDcyNDUyLDEyNC4wNDM0NzUyNzUxNjA3NCwtMTEyOTg2MTc1NywtMSwtMjIzMzcwNzE0LFczc2libUZ0WlNJNklsQkVSaUJXYVdWM1pYSWlMQ0prWlhOamNtbHdkR2x2YmlJNklsQnZjblJoWW14bElFUnZZM1Z0Wlc1MElFWnZjbTFoZENJc0ltMXBiV1ZVZVhCbGN5STZXM3NpZEhsd1pTSTZJbUZ3Y0d4cFkyRjBhVzl1TDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMHNleUowZVhCbElqb2lkR1Y0ZEM5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlYWDBzZXlKdVlXMWxJam9pUTJoeWIyMWxJRkJFUmlCV2FXVjNaWElpTENKa1pYTmpjbWx3ZEdsdmJpSTZJbEJ2Y25SaFlteGxJRVJ2WTNWdFpXNTBJRVp2Y20xaGRDSXNJbTFwYldWVWVYQmxjeUk2VzNzaWRIbHdaU0k2SW1Gd2NHeHBZMkYwYVc5dUwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjBzZXlKMGVYQmxJam9pZEdWNGRDOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5WFgwc2V5SnVZVzFsSWpvaVEyaHliMjFwZFcwZ1VFUkdJRlpwWlhkbGNpSXNJbVJsYzJOeWFYQjBhVzl1SWpvaVVHOXlkR0ZpYkdVZ1JHOWpkVzFsYm5RZ1JtOXliV0YwSWl3aWJXbHRaVlI1Y0dWeklqcGJleUowZVhCbElqb2lZWEJ3YkdsallYUnBiMjR2Y0dSbUlpd2ljM1ZtWm1sNFpYTWlPaUp3WkdZaWZTeDdJblI1Y0dVaU9pSjBaWGgwTDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMWRmU3g3SW01aGJXVWlPaUpOYVdOeWIzTnZablFnUldSblpTQlFSRVlnVm1sbGQyVnlJaXdpWkdWelkzSnBjSFJwYjI0aU9pSlFiM0owWVdKc1pTQkViMk4xYldWdWRDQkdiM0p0WVhRaUxDSnRhVzFsVkhsd1pYTWlPbHQ3SW5SNWNHVWlPaUpoY0hCc2FXTmhkR2x2Ymk5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlMSHNpZEhsd1pTSTZJblJsZUhRdmNHUm1JaXdpYzNWbVptbDRaWE1pT2lKd1pHWWlmVjE5TEhzaWJtRnRaU0k2SWxkbFlrdHBkQ0JpZFdsc2RDMXBiaUJRUkVZaUxDSmtaWE5qY21sd2RHbHZiaUk2SWxCdmNuUmhZbXhsSUVSdlkzVnRaVzUwSUVadmNtMWhkQ0lzSW0xcGJXVlVlWEJsY3lJNlczc2lkSGx3WlNJNkltRndjR3hwWTJGMGFXOXVMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4wc2V5SjBlWEJsSWpvaWRHVjRkQzl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOVhYMWQsV3lKeWRTMVNWU0pkLDAsMSwwLDI0LDIzNzQxNTkzMCw4LDIyNzEyNjUyMCwwLDEsMCwtNDkxMjc1NTIzLFIyOXZaMnhsSUVsdVl5NGdUbVYwYzJOaGNHVWdSMlZqYTI4Z1YybHVNeklnTlM0d0lDaFhhVzVrYjNkeklFNVVJREV3TGpBN0lGZHBialkwT3lCNE5qUXBJRUZ3Y0d4bFYyVmlTMmwwTHpVek55NHpOaUFvUzBoVVRVd3NJR3hwYTJVZ1IyVmphMjhwSUVOb2NtOXRaUzh4TWprdU1DNHdMakFnVTJGbVlYSnBMelV6Tnk0ek5pQXlNREF6TURFd055Qk5iM3BwYkd4aCxleUpqYUhKdmJXVWlPbnNpWVhCd0lqcDdJbWx6U1c1emRHRnNiR1ZrSWpwbVlXeHpaU3dpU1c1emRHRnNiRk4wWVhSbElqcDdJa1JKVTBGQ1RFVkVJam9pWkdsellXSnNaV1FpTENKSlRsTlVRVXhNUlVRaU9pSnBibk4wWVd4c1pXUWlMQ0pPVDFSZlNVNVRWRUZNVEVWRUlqb2libTkwWDJsdWMzUmhiR3hsWkNKOUxDSlNkVzV1YVc1blUzUmhkR1VpT25zaVEwRk9UazlVWDFKVlRpSTZJbU5oYm01dmRGOXlkVzRpTENKU1JVRkVXVjlVVDE5U1ZVNGlPaUp5WldGa2VWOTBiMTl5ZFc0aUxDSlNWVTVPU1U1SElqb2ljblZ1Ym1sdVp5SjlmWDE5LDY1LDUyMTA1MTkxMSwxLDEsLTEsMTY5OTk1NDg4NywxNjk5OTU0ODg3LC0yMDc1NjQwOTA3LDg=; abt_data=7.pIfhIf1er7UWuBs9P3YEXVz6qUvoVhNKTdxTcxnkJxsGuMIwFOKzf0sNnAIxOfve465P46ShE0uKoxqovxDpIpZSDWmEVckkobIfgM4c8y-0b_urzRNIGTngXVrDKQjtHRnVFNuADYgLQ-kEU1x4bf3q8OY2Q3OJxp2G_Seh3YoVPoGYL2e3S9yLLysmKDDYwHUKkP-bP1miaCSNY5AAyMQbArATnHgi7Hf0VPsiCq6zq_ariub4uEDf_S71o3rKb28KFvvo3V1yGhR0fRpTppRmWIpNsLbQTGt3nIoRYDCxmjaEiO1UyF_VtKnwa-wWDi32-MWmott-JWx7b2ZxXqyWg4Gepg9DTGhF4wAiGXTgnxIrt0U3BlQB1F08PVD0plOO0UTDk8udAbiusdwt3XnpMcetZK9tSX8OgGm8hAC-IXVey0F8-ldohqmGiLOG_Hd4riGDDZHe65p-8oy_e8JJ9D6DkDbCxL4-9DC2KaNTXt9VoDXFBIpvJrFW9MQ7c_T4Kv5bFNrShaQyibY; ADDRESSBOOKBAR_WEB_CLARIFICATION=1729458479',
#     'priority': 'u=0, i',
#     'referer': 'https://www.ozon.ru/?__rr=1&abt_att=1&origin_referer=www.google.com',
#     'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'service-worker-navigation-preload': 'true',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
# }
#
# params = {
#     'avtc': '1',
#     'avte': '4',
#     'avts': '1729458023',
# }
#
# response = rq.get(
#     'https://www.ozon.ru/product/uvlazhnyayushchiy-universalnyy-krem-nivea-cr-me-dlya-litsa-ruk-i-tela-s-pantenolom-250-ml-5043850/',
#     params=params,
#     cookies=cookies,
#     headers=headers,
# )
# soup = BeautifulSoup(response.content, "lxml")
#
# title = soup.find('h1', class_='tm4_27 tsHeadline550Medium')
# print(title.text)

# driver = webdriver.Chrome()
# driver.get('https://www.maxidom.ru/catalog/dushevye-sistemy/1001529332/')
# soup = BeautifulSoup(driver.page_source, 'lxml')
# price = soup.find('div', class_='lvl1__product-body-buy-price-base')
# print(price['data-repid_price'])