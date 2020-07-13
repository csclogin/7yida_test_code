# -*- coding: utf-8 -*-
# #  author caishicheng
import requests
url = "https://jpgatewaycs.517la.com/h5/HOTELSELLINTERFACEWEB/api/queryHotelListNew"

payload = "{\"keyWordType\":3,\"keyWord\":\"7天\",\"cityCode\":\"001018001\",\"countryName\":\"中国\",\"provinceName\":\"四川\",\"cityName\":\"CHENGDU\",\"city\":\"成都\",\"checkInDate\":\"2020-01-01\",\"checkOutDate\":\"2020-01-02\",\"personOrCompay\":2,\"score\":\"\",\"Distance\":0,\"addressType\":1,\"latitude\":30.679943,\"longitude\":104.067923,\"location\":\"成都市青羊区王家塘街\",\"isOverCity\":0,\"filterSelectInfo\":{\"Distance\":0,\"brandName\":\"7天\",\"hotelAmenity\":\"\"},\"hotelAmenity\":\"\",\"brandName\":\"7天\",\"locationInfo\":{\"latitude\":30.679943,\"longitude\":104.067923,\"address\":\"成都市青羊区王家塘街\"},\"sortName\":\"综合\",\"CooperativeHotel\":0,\"undefined\":0,\"comsubSidiary\":0,\"matchStandard\":0,\"IncludeBreakfast\":0,\"CancelFree\":0,\"SureAtOnce\":0,\"standardPrice\":null,\"brandGroup\":\"\",\"brandNameByGroup\":\"\",\"hotelType\":\"\",\"featureTheme\":\"\",\"pageSize\":10,\"pageNo\":1,\"queryTimeStamp\":\"1577349602339\"}"
headers = {
    'auth': "FBA0FE18796EEFFBAD30A330117D7D79C0EB7FD714677005858EE262C185BE4EE0D798465454EC182141DD41A436909E5080C86EC6603B60AF66759EBDDF1158",
    'Content-Type': "application/json;charset=UTF-8",
    'la517_authSign': "FBA0FE18796EEFFBAD30A330117D7D79C0EB7FD714677005858EE262C185BE4EE0D798465454EC182141DD41A436909E5080C86EC6603B60AF66759EBDDF1158",
    'la517_clientInfo': "eyJwa2duYW1lIjoiY29tLm5hNTE3LkNMQWlyVGlja2V0SDUiLCJjbGllbnR0eXBlIjozLCJtY29kZSI6IiIsInRpbWVzdGFtcCI6IjIwMTktMTItMjYgMTY6NDA6MDIiLCJ2ZXJzaW9uIjoiODE0MCJ9",
    'la517_clientType': "201",
    'la517_requestid': "1577349602356",
    'User-Agent': "PostmanRuntime/7.19.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "f2707744-9d67-4726-aeff-7431ca8a62df,87d17277-cc5c-43c8-a0a0-cd77208c4c87",
    'Host': "jpgatewaycs.517la.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "862",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)