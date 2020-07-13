# -*- coding: utf-8 -*-
#  author caishicheng


import requests
import unittest
import json
from API_test.common import api_data,method_get_data


class Hotel_queryStandard(unittest.TestCase):
	def setUp(self):
		print('开始测试')
	def test_queryStandard(self):
		url=r'https://'+api_data.Host+r"/h5/HOTELEXTERNALINTERACTIONSERVICE/api/queryStandard"
		data={"takeOffTime":"2020-07-21 12:00:00","subStandardType":3,"staffInfoVoList":[{"staffID":"20190923134348848187","positionID":"","travelScene":"1"},{"staffID":"20190923134348848187","positionID":"","travelScene":"2"}]}
		headers={
  'Content-Type': 'application/json;charset=UTF-8',
  'la517_authSign': api_data.la517_authSign,
  'la517_clientInfo': api_data.la517_clientInfo,
  'la517_clientType': api_data.la517_clientType,
}
		response = requests.request("POST", url, headers=headers, data=json.dumps(data))
		print(response.text)
		if response.status_code==200:
			self.assertIn('查询成功',response.text)
		else:
			print('测试失败')
	def tearDown(self):
		pass
if __name__=='__main__':
	unittest.main()