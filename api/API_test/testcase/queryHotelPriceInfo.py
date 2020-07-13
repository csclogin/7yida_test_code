# -*- coding: utf-8 -*-
#  author caishicheng


import requests
import unittest
import json
from API_test.common import api_data,method_get_data
import time


class Hotel_queryHotelPriceInfo(unittest.TestCase):
	def setUp(self):
		print('开始测试')
	def test_queryHotelPriceInfo(self):
		url=r'https://'+api_data.Host+r"/h5/HOTELSELLINTERFACEWEB/api/queryHotelPriceInfo"
		data={"TMCDeptID":"20160512144219375328","sellPlat":4,"checkInDate":api_data.checkInDate,"checkOutDate":
			api_data.checkOutDate,"checkInType":2,"hotelCode":method_get_data.get_HotelID(),"cityCode":"001001001","invoiceType":2,
			  "CompanyAccount":"20180316100422666114","purchaseAccount":"20190923122037633478","onlyWaitOne":'false',
			  "isActual":'true',"roomCount":1,"adultCount":1,"childCount":0,"childAges":[]}
		headers={
  'Content-Type': 'application/json;charset=UTF-8',
  'la517_authSign': api_data.la517_authSign,
  'la517_clientInfo': api_data.la517_clientInfo,
  'la517_clientType': api_data.la517_clientType,
}
		response = requests.request("POST", url, headers=headers, data=json.dumps(data))
		print(response.text)
		if response.status_code==200:
			self.assertIn('成功',response.text)
			self.assertIn('HotelCode', response.text)
		else:
			print('测试失败')
	def tearDown(self):
		pass
if __name__=='__main__':
	unittest.main()