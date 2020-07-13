# -*- coding: utf-8 -*-
#  author caishicheng


import requests
import unittest
import json
from API_test.common import api_data,method_get_data
import time


class Hotel_queryHotelRoom(unittest.TestCase):
	def setUp(self):
		print('开始测试')
	def test_queryHotelRoom(self):
		url=r'https://'+api_data.Host+r"/h5/HOTELSELLINTERFACEWEB/api/queryHotelRoom"
		data={"hotelCode":method_get_data.get_HotelID(),"cityCode":"001001001"}
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
			self.assertIn('HotelName', response.text)
		else:
			print('测试失败')
	def tearDown(self):
		pass
if __name__=='__main__':
	unittest.main()