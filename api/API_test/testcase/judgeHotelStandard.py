# encoding=utf-8
#  author caishicheng


import requests
import unittest
import json
from API_test.common import api_data,method_get_data
import urllib3


class Hotel_judgeHotelStandard(unittest.TestCase):
	def setUp(self):
		print('开始测试')
	def test_judgeHotelStandard(self):
		url=r'https://'+api_data.Host+r"/h5/HOTELEXTERNALINTERACTIONSERVICE/api/judgeHotelStandard"
		headers = {
			'Content-Type': 'application/json;charset=UTF-8',
			'la517_authSign': api_data.la517_authSign,
			'la517_clientInfo': api_data.la517_clientInfo,
			'la517_clientType': api_data.la517_clientType,}
		data={"staffInfoVoList":[{"staffID":"20190923134348848187","staffName":"\u8521\u4e16\u6210","mainAppInfoID":"","directDepartList":["20180316100422666114"],"roomIndex":''}],
	"cityCode":"001001001",
	"cityName":"\u5317\u4eac",
	"beginDate":api_data.checkInDate,
	"endDate":api_data.checkOutDate,
	"price":method_get_data.get_AveragePrice(),
	"totalPrice":method_get_data.get_AveragePrice(),
	"isProtocolHotel":1,
	"travelScene":"1",
	"zoneName":"\u671d\u9633\u533a",
	"orderType":0,
	"function":"A",
	"hotelID":method_get_data.get_HotelID(),
	"roomID":method_get_data.get_RoomID(),
	"ratePlanID":method_get_data.get_RatePlanID(),
	"hotelStarType":"1",
	"priceType":1,
	"channelID":method_get_data.get_ChannelID()}
		print(data)
		response = requests.request('POST',url,headers=headers,data=json.dumps(data))
		print(response.text)
		if response.status_code==200:
			self.assertIn('成功', response.text)
		else:
			print('测试失败')
	def tearDown(self):
		pass
if __name__=='__main__':
	unittest.main()