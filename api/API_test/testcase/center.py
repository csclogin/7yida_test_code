# -*- coding: utf-8 -*-
#  author caishicheng

import requests
import unittest
import json
from API_test.common import api_data


class Hotel_querySubway(unittest.TestCase):
	def setUp(self):
		print('开始测试')
	def test_querySubway(self):
		url=r'https://'+api_data.Host1+r"/companycostcenter/%7B%22staffNos%22:[%2220190923134348848187%22]%7D"
		headers={ 'auth': api_data.la517_authSign,}
		response = requests.request("GET", url, headers=headers)
		print(response.text)
		if response.status_code==200:
			self.assertIn('成功',response.text)
		else:
			print('测试失败')
	def tearDown(self):
		pass
if __name__=='__main__':
	unittest.main()