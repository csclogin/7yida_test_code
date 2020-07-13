# -*- coding: utf-8 -*-
#  author caishicheng


import requests
import unittest
import json
from API_test.common import api_data


class Hotel_getStandardInfo(unittest.TestCase):
	def setUp(self):
		print('开始测试')
	def test_getStandardInfo(self):
		url=r'https://'+api_data.Host+r"/h5/CLAIRTICKETEXTERNALINTERACTIONSERVICE/jppubapi/rapidDevelop/getStandardInfo"
		data={"standardType":3,"travelScene":"","judgeHotel":'false',"subStandardType":3,"takeOffTime":api_data.now_day}
		headers={
  'Content-Type': 'application/json;charset=utf-8',
  'Host': api_data.Host,
	'auth':api_data.la517_authSign,
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