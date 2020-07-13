# -*- coding: utf-8 -*-
#  author caishicheng


import requests
import unittest
import json
from API_test.common import api_data,method_get_data
import time


class Hotel_queryHotelListNew(unittest.TestCase):
	def setUp(self):
		print('开始测试')
	def test_queryHotelListNew(self):
		url=r'https://'+api_data.Host+r"/h5/HOTELSELLINTERFACEWEB/api/queryHotelListNew"
		data={"keyWordsInfo":{"input":"\u5317\u4eac\u8721\u7b14\u5c0f\u65b0\u9752\u5e74\u516c\u5bd3","query":"\u5317\u4eac\u8721\u7b14\u5c0f\u65b0\u9752\u5e74\u516c\u5bd3","lat":"","lng":"","type":4},"keyWord":"\u5317\u4eac\u8721\u7b14\u5c0f\u65b0\u9752\u5e74\u516c\u5bd3","keyWordType":4,"cityCode":"001001001","countryName":"\u4e2d\u56fd","provinceName":"\u5317\u4eac","cityName":"BEIJING","city":"\u5317\u4eac","checkInDate":api_data.checkInDate,"checkOutDate":api_data.checkOutDate,"personOrCompay":2,"score":"","Distance":0,"addressType":0,"latitude":"","longitude":"","location":"","isOverCity":0,"filterSelectInfo":{"Distance":0,"brandName":"","hotelAmenity":""},"hotelAmenity":"","brandName":"","sortName":"综合","standardPrice":352,"brandGroup":"","brandNameByGroup":"","hotelType":"","featureTheme":"","pageSize":10,"pageNo":1,"queryTimeStamp":"1589539312429"}
		headers={
  'Content-Type': 'application/json;charset=UTF-8',
	'la517_authSign':api_data.la517_authSign,
  'la517_clientInfo': api_data.la517_clientInfo,
  'la517_clientType': api_data.la517_clientType,
}
		print(url)
		print(data)
		print(headers)
		response = requests.request("POST", url, headers=headers, data=json.dumps(data))
		print(response.text)
		if response.status_code==200:
			self.assertIn('查询成功',response.text)
			self.assertIn('HotelID', response.text)
		else:
			print('测试失败')
	def tearDown(self):
		pass
if __name__=='__main__':
	unittest.main()