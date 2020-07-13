# -*- coding: utf-8 -*-
#  author caishicheng
import re
import requests,json
from API_test.common import api_data
import time


##获取auth

def get_auth():
    url = "https://www.517la.com/Home/getAuthSignByUserNoForCloud"
    data = {}
    headers = {
        'Cookie': 'acw_tc=2760827815925563972233555e84546a497422421cc35e319b0a88f229d10b; '
                  'JSESSIONID=C948713F1563A9F7803AE4D2E84C57E3; __wpkreporterwid_=7f30e867-4610-466a-a429-343cf38fbb90; '
                  'qimo_seosource_34b2ea00-974c-11e9-84ff-034b0e5b1250=%E7%AB%99%E5%86%85; '
                  'qimo_seokeywords_34b2ea00-974c-11e9-84ff-034b0e5b1250=; '
                  'href=https%3A%2F%2Fwww.517la.com%2F; accessId=34b2ea00-974c-11e9-84ff-034b0e5b1250; '
                  'pageViewNum=1; clbussuerName=; Hm_lvt_daffad6c1042cce8d8e763cad4e10d43=1592555626;'
                  ' Hm_lpvt_daffad6c1042cce8d8e763cad4e10d43=1592556399; bad_id34b2ea00-974c-11e9-84ff-034b0e5b1250=64366e41-b209-11ea-b3d5-117c3bd14c24; '
                  'nice_id34b2ea00-974c-11e9-84ff-034b0e5b1250=64366e42-b209-11ea-b3d5-117c3bd14c24; '
                  'acw_tc=2760826415925569379082300e2792e1539adb2558e57ff9a68c4cf2438fee; '
                  'cl_loginSign=ftD5V1wZxf8kdTJlohi%2FcQ%3D%3D; cl_loginKey=ftD5V1wZxf%2BQNjxuwiu1Rw%3D%3D; '
                  'cl_loginKey1=uIH2QudNkFN2meVnvuW58%2BSPfov2mdFAA5lrMT4jDkGp15v35sW7jg%3D%3D; '
                  'cl_loginKey2=vKU9qmGQv20Q3P6vlAy5li%2FkVQ7aV4Jg; cl_loginKey3=3u745qLLQO86rGQgcAVUAA%3D%3D',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    # print(headers)
    response = requests.request("POST", url, headers=headers, data=data)
    print(response.text)
get_auth()

##获取标准金额
def get_standardPrice():
    url=r'https://' + api_data.Host + r"/h5/HOTELSELLINTERFACEWEB/api/queryHotelStandard"
    data = {"travelType": 1, "cityCode": "001001001", "checkInDate": api_data.checkInDate,
            "checkOutDate":api_data.checkOutDate}
    headers = {
        'Content-Type': 'application/json;charset=utf-8',
        'Host': api_data.Host,
        'la517_authSign': api_data.la517_authSign,
        'la517_clientType': api_data.la517_clientType,
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
    text = response.text
    standardPrice=re.findall(r'{\\"flag\\":1,\\"price\\":(.+?),\\"remark\\":\\"\\"}}',text)[0]
    return standardPrice

##根据测试host地址是正式还是测试 取得地址
def get_url():
    if api_data.Host=='hotelgateaway.517la.com':
        url='https://m.517la.com'
    elif api_data.Host=='jpgatewaycs.517la.com':
        url = 'https://cs_m.517la.com'


def get_HotelID():   ##HotelID
    url = r'https://' + api_data.Host + r"/h5/HOTELSELLINTERFACEWEB/api/queryHotelListNew"
    data = {"keyWordsInfo": {"input": "北京蜡笔小新青年公寓", "query": "北京蜡笔小新青年公寓", "lat": "", "lng": "", "type": 4},
            "keyWord": "北京蜡笔小新青年公寓", "keyWordType": 4, "cityCode": "001001001", "countryName": "中国",
            "provinceName": "北京", "cityName": "BEIJING", "city": "北京", "checkInDate": "2020-07-30",
            "checkOutDate": "2020-07-31", "personOrCompay": 2, "score": "", "Distance": 0, "addressType": 0,
            "latitude": "", "longitude": "", "location": "", "isOverCity": 0,
            "filterSelectInfo": {"Distance": 0, "brandName": "", "hotelAmenity": ""}, "hotelAmenity": "",
            "brandName": "", "sortName": "综合", "standardPrice": 352, "brandGroup": "", "brandNameByGroup": "",
            "hotelType": "", "featureTheme": "", "pageSize": 10, "pageNo": 1, "queryTimeStamp": "1589539312429"}
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'auth': api_data.la517_authSign,
        'la517_authSign': api_data.method_get_data.get_auth(),
        'la517_clientInfo': api_data.la517_clientInfo,
        'la517_clientType': api_data.la517_clientType,
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
    HotelID=re.findall(r'HotelID\\\\\\":\\\\\\"(.+?)\\\\\\",\\\\\\"HotelNo',response.text)[0]
    return HotelID


def get_RoomID():  ##获取RoomID
    url = r'https://' + api_data.Host + r"/h5/HOTELSELLINTERFACEWEB/api/queryHotelPriceInfo"
    data = {"TMCDeptID": "20160512144219375328", "sellPlat": 4, "checkInDate": api_data.checkInDate, "checkOutDate":
        api_data.checkOutDate, "checkInType": 2, "hotelCode": get_HotelID(), "cityCode": "001001001",
            "invoiceType": 2,
            "CompanyAccount": "20180316100422666114", "purchaseAccount": "20190923122037633478", "onlyWaitOne": 'false',
            "isActual": 'true', "roomCount": 1, "adultCount": 1, "childCount": 0, "childAges": []}
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'auth': api_data.la517_authSign,
        'la517_authSign': api_data.la517_authSign,
        'la517_clientInfo': api_data.la517_clientInfo,
        'la517_clientType': api_data.la517_clientType,
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
    RoomID=re.findall(r'RoomID\\":\\"(.+?)\\",\\"RoomName',response.text)[0]
    return RoomID

def get_RatePlanID(): ##获取RatePlanID的方法
    url = r'https://' + api_data.Host + r"/h5/HOTELSELLINTERFACEWEB/api/queryHotelPriceInfo"
    data = {"TMCDeptID": "20160512144219375328", "sellPlat": 4, "checkInDate": api_data.checkInDate, "checkOutDate":
        api_data.checkOutDate, "checkInType": 2, "hotelCode": get_HotelID(), "cityCode": "001001001",
            "invoiceType": 2,
            "CompanyAccount": "20180316100422666114", "purchaseAccount": "20190923122037633478", "onlyWaitOne": 'false',
            "isActual": 'true', "roomCount": 1, "adultCount": 1, "childCount": 0, "childAges": []}
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'auth': api_data.la517_authSign,
        'la517_authSign': api_data.la517_authSign,
        'la517_clientInfo': api_data.la517_clientInfo,
        'la517_clientType': api_data.la517_clientType,
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
    RatePlanID=re.findall(r'RatePlanID\\":\\"(.+?)\\",\\"RoomTypeId',response.text)[0]
    return RatePlanID


def get_ChannelID():##获取ChannelID的方法
    url = r'https://' + api_data.Host + r"/h5/HOTELSELLINTERFACEWEB/api/queryHotelPriceInfo"
    data = {"TMCDeptID": "20160512144219375328", "sellPlat": 4, "checkInDate": api_data.checkInDate, "checkOutDate":
        api_data.checkOutDate, "checkInType": 2, "hotelCode": get_HotelID(), "cityCode": "001001001",
            "invoiceType": 2,
            "CompanyAccount": "20180316100422666114", "purchaseAccount": "20190923122037633478", "onlyWaitOne": 'false',
            "isActual": 'true', "roomCount": 1, "adultCount": 1, "childCount": 0, "childAges": []}
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'auth': api_data.la517_authSign,
        'la517_authSign': api_data.la517_authSign,
        'la517_clientInfo': api_data.la517_clientInfo,
        'la517_clientType': api_data.la517_clientType,
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
    ChannelID=re.findall(r'ChannelID\\":\\"(.+?)\\",\\"OriginChannelID',response.text)[0]
    return ChannelID

def get_PlanID():##获取PlanID的方法
    url = r'https://' + api_data.Host + r"/h5/HOTELSELLINTERFACEWEB/api/queryHotelPriceInfo"
    data = {"TMCDeptID": "20160512144219375328", "sellPlat": 4, "checkInDate": api_data.checkInDate, "checkOutDate":
        api_data.checkOutDate, "checkInType": 2, "hotelCode": get_HotelID(), "cityCode": "001001001",
            "invoiceType": 2,
            "CompanyAccount": "20180316100422666114", "purchaseAccount": "20190923122037633478", "onlyWaitOne": 'false',
            "isActual": 'true', "roomCount": 1, "adultCount": 1, "childCount": 0, "childAges": []}
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'auth': api_data.la517_authSign,
        'la517_authSign': api_data.la517_authSign,
        'la517_clientInfo': api_data.la517_clientInfo,
        'la517_clientType': api_data.la517_clientType,
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
    PlanID = re.findall(r'PlanID\\":\\"(.+?)\\",\\"AveragePrice', response.text)[0]
    return PlanID

def get_AveragePrice():##获取AveragePrice的方法
    url = r'https://' + api_data.Host + r"/h5/HOTELSELLINTERFACEWEB/api/queryHotelPriceInfo"
    data = {"TMCDeptID": "20160512144219375328", "sellPlat": 4, "checkInDate": api_data.checkInDate, "checkOutDate":
        api_data.checkOutDate, "checkInType": 2, "hotelCode": get_HotelID(), "cityCode": "001001001",
            "invoiceType": 2,
            "CompanyAccount": "20180316100422666114", "purchaseAccount": "20190923122037633478", "onlyWaitOne": 'false',
            "isActual": 'true', "roomCount": 1, "adultCount": 1, "childCount": 0, "childAges": []}
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'auth': api_data.la517_authSign,
        'la517_authSign': api_data.la517_authSign,
        'la517_clientInfo': api_data.la517_clientInfo,
        'la517_clientType': api_data.la517_clientType,
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
    AveragePrice = re.findall(r'AveragePrice\\":(.+?),\\"AveragePeice', response.text)[0]
    return AveragePrice
# def get_la517_authSign():
#     url='http://test.517la.com/Home/getAuthSignByUserNoForCloud'
#     payload = {}
#     headers = {
#         'Cookie': '__wpkreporterwid_=cd2a48d6-bef7-449f-181a-091be623b6f3; Hm_lvt_daffad6c1042cce8d8e763cad4e10d43=1589958397; href=http%3A%2F%2Ftest.517la.com%2F; accessId=34b2ea00-974c-11e9-84ff-034b0e5b1250; bad_id34b2ea00-974c-11e9-84ff-034b0e5b1250=190c8a71-9a68-11ea-b3d5-117c3bd14c24; nice_id34b2ea00-974c-11e9-84ff-034b0e5b1250=190c8a72-9a68-11ea-b3d5-117c3bd14c24; clbussuerName=; CookieUser=undefined; cl_uk=c6Z%2BFT5ewdH9xM4K4vxFkmb%2Foexuo0xLOG75ZUg5%2FCKFoe1ninqTW7%2FDmWZhX5dcvBXcn2gVJNQ3%0A0vOKxvSgbwFvaxaRAm94cVNg%2FQq8Bketg8r9QyQJom1s%2FDN0S%2Frm9NkHHy2%2BLSdfw78LHt7TR2iZ%0AF1jpcuYPxGie8TCzwrkD4%2BLAbjykO74TypjE3OyxBdKShHsaI%2F9Yz2jW%2FD4YT%2BwCbzPOg1cw49%2FH%0A84BcY2OE9hqT48vZbSB78eW16QL%2BHuyS2BiK8BovLCroROFsbdVqkfXVLmDNXSmRT%2BzEU246%2B7fG%0A3vO5DRi%2FY83T%2BDxUF%2BW6nf9Xo3OUkEeYnHY3NKKGx1ng%2BCDdZv51id8bX5isLsKQEgLoHBo1pRnb%0A6kxXdeYTpvOXR3lKaZu3%2FsfK9%2Fiz12WvEbzlKja46%2FwJrntSgTab%2FrXgENHb2I4QIy%2Fgt5OAdoKy%0AT968gg7qWmn2axGoJRINDcBmDOmfg3AuPAYBQF%2FLeBnH2y17IvXdCNd3qdeb9%2BbFu44%3D; cl_entno=20180316100422666114; CLBussUserWebFirst=01; u={"sessionID":"5a243ab2-a6e4-42d1-bae1-20387bae175f2","entNo":"20180316100422666114","tmcNo":"20160512144219375328","userNo":"20190923122037633478","staffNo":"20190923134348848187","url":"stcs_m.517la.com","userName":"%E8%94%A1%E4%B8%96%E6%88%90"}; cl_sid=5a243ab2-a6e4-42d1-bae1-20387bae175f2; JSESSIONID=EFEDB6A9841626C530823D5947BF187E; qimo_seosource_34b2ea00-974c-11e9-84ff-034b0e5b1250=%E7%AB%99%E5%86%85; qimo_seokeywords_34b2ea00-974c-11e9-84ff-034b0e5b1250=; cl_loginSign=ftD5V1wZxf8kdTJlohi%2FcQ%3D%3D; cl_loginKey=ftD5V1wZxf%2BQNjxuwiu1Rw%3D%3D; cl_loginKey1=uIH2QudNkFN2meVnvuW58%2BSPfov2mdFAA5lrMT4jDkGp15v35sW7jg%3D%3D; cl_loginKey2=vKU9qmGQv20Q3P6vlAy5li%2FkVQ7aV4Jg; cl_loginKey3=jnhYfWr0rkB2FTvjYu6mHA%3D%3D; CLBussUserWeb=0; Hm_lpvt_daffad6c1042cce8d8e763cad4e10d43=1589969861; pageViewNum=13'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#     return response.text
# get_la517_authSign()