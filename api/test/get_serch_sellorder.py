# -*- coding: utf-8 -*-
#  author caishicheng
import requests

url = "http://ptcs.hotel.517na.com/HotelOrder/SellOrderRequest"

querystring = {"pageIndex":"1","selectTime":"2019%E5%B9%B410%E6%9C%88","createOrderBeginTime":"2019-10-24","createOrderEndTime":"2019-10-25","checkinBeginTime":"","checkinEndTime":"","checkoutBeginTime":"","checkoutEndTime":"","gust":"","orderNum":"","hotelName":"","companyName":"","city":"","orderStatus":"0","sellPlat":"0","bookMan":"","payType":"0","paperType":"0","support":"","xianXiaOrder":"0","orderType":"","supplyName":"","modifyOrder":"","companyPayStatus":"","personPayStatus":""}

headers = {
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "a21c6ffb-7023-4447-9356-0d78da0c4672,dd504589-3437-441e-8e21-3567b077e22b",
    'Host': "ptcs.hotel.517na.com",
    'Cookie': "ASP.NET_SessionId=vpdwh0giejkwdjz5qr2wphnn; AutomationServicePlat=F800673141E86F77B29D0F7CB80912EAEA304E7E0FFC8188E68F8C3F3DD6D5A68BB1B1B927D23A3C37BC4CD046D336A9263B239A6D3B02F1A03A904A4C074AF9F999AF58CC716AE863491D8766D27891B9B9AB4B464DC93001442C140D0A54CA9EEEAE87CC4853536854EED8BE6951FF",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text) 