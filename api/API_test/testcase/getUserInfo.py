# -*- coding: utf-8 -*-
#  author caishicheng


import requests
import unittest
import json
from API_test.common import api_data


class Hotel_getUserInfo(unittest.TestCase):
	def setUp(self):
		print('开始测试')
	def test_getUserInfo(self):
		url=r'https://'+api_data.Host1+r"/getUserInfo"
		data = {}
		headers={
  'Content-Type': 'application/json;charset=utf-8',
  'auth': api_data.la517_authSign,
}
		response = requests.request("GET", url, headers=headers,data=data)
		print(response.text)
		if response.status_code==200:
			self.assertIn('tMCNumber',response.text)
		else:
			print('测试失败')
	def tearDown(self):
		pass
if __name__=='__main__':
	unittest.main()