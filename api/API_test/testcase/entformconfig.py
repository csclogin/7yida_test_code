# -*- coding: utf-8 -*-
#  author caishicheng


import requests
import unittest
import json
from API_test.common import api_data


class Hotel_entformconfig(unittest.TestCase):
	def setUp(self):
		print('开始测试')
	def test_getUserInfo(self):
		url=r'https://'+api_data.Host1+r"./entformconfig/%7B%22isDelete%22%3A%220%22%2C%22isEnabled%22%3A%221%22%2C%22bussType%22%3A%221%22%2C%22formID%22%3A%22Order_Fill%22%7D"
		data = {}
		headers={
  'Content-Type': 'application/json;charset=utf-8',
  'auth': api_data.la517_authSign,
}
		response = requests.request("GET", url, headers=headers,data=data)
		print(response.text)
		if response.status_code==200:
			self.assertIn('查询成功',response.text)
		else:
			print('测试失败')
	def tearDown(self):
		pass
if __name__=='__main__':
	unittest.main()
