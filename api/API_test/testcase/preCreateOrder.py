# -*- coding: utf-8 -*-
#  author caishicheng


import requests
import unittest
import json
from API_test.common import api_data,method_get_data
import time


class Hotel_preCreateOrder(unittest.TestCase):
	def setUp(self):
		print('开始测试')
	def test_preCreateOrder(self):
		url=r'https://'+api_data.Host+r"/h5/HOTELSELLINTERFACEWEB/api/preCreateOrder"
		data={
	"ratePlanID": method_get_data.get_RatePlanID(),
	"checkInDate": api_data.checkInDate,
	"checkOutDate": api_data.checkOutDate,
	"channelID": method_get_data.get_ChannelID(),
	"platenoMemCook": "",
	"purchaseAccount": "20190923122037633478",
	"hotelID": method_get_data.get_HotelID(),
	"baseRoomTypeID": method_get_data.get_RoomID(),
	"entNo": "20180316100422666114",
	"baseHotelCode": method_get_data.get_HotelID(),
	"bindUser": "",
	"latestArrivalTime": api_data.checkOutDate+" 22:00:00",
	"guestCount": "1",
	"roomTypeID": method_get_data.get_RoomID(),
	"roomCount": 1,
	"adultCount": 1,
	"childCount": 0,
	"childAges": []
}
		headers={
  'Content-Type': 'application/json;charset=UTF-8',
	'auth':api_data.la517_authSign,
  'la517_authSign': api_data.la517_authSign,
  'la517_clientInfo': api_data.la517_clientInfo,
  'la517_clientType': api_data.la517_clientType,
}
		response = requests.request("POST", url, headers=headers, data=json.dumps(data))
		print(response.text)
		if response.status_code==200:
			self.assertIn('成功',response.text)
			self.assertIn('PreBookResult\\":1', response.text)
		else:
			print('测试失败')
	def tearDown(self):
		pass
if __name__=='__main__':
	unittest.main()