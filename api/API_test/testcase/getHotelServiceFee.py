# -*- coding: utf-8 -*-
#  author caishicheng



import requests
import unittest
import json
from API_test.common import api_data,method_get_data


class Hotel_getHotelServiceFee(unittest.TestCase):
	def setUp(self):
		print('开始测试')
	def test_getHotelServiceFee(self):
		url=r'https://'+api_data.Host+r"/h5/HOTELSELLINTERFACEWEB/api/getHotelServiceFee"
		data={"travelT":"0","deleT":0,"bookT":3,"ticketT":5,"supplyID":"20180225141148567561","isSelfComptPrice":1}
		headers={
  'Content-Type': 'text/plain',
  'Host': api_data.Host,
  'la517_authSign': api_data.la517_authSign,
  'la517_clientInfo': api_data.la517_clientInfo,
  'la517_clientType': api_data.la517_clientType,
}
		response = requests.request("POST", url, headers=headers, data=json.dumps(data))
		print(response.text)
		if response.status_code==200:
			self.assertIn('成功', response.text)
			self.assertIn('body', response.text)
		else:
			print('测试失败')
	def tearDown(self):
		pass
if __name__=='__main__':
	unittest.main()