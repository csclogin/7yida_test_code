# -*- coding: utf-8 -*-
#  author caishicheng



import requests
import unittest
import json
from API_test.common import api_data,method_get_data


class Hotel_commonPassengersForCloud(unittest.TestCase):
	def setUp(self):
		print('开始测试')
	def test_commonPassengersForCloud(self):
		url=r'https://'+api_data.Host+r"/h5/HOTELSELLINTERFACEWEB/api/commonPassengersForCloud"
		data={"bookingUserInfo":{"staffID":"20190923134348848187","staffName":"蔡世成","departmentID":"20180316100422666114","departmentName":"思存测试企业","companyID":"20180316100422666114","companyName":"思存测试企业","tMCID":"20160512144219375328","tMCName":"四川海岛印象旅行社有限公司","userNo":"20190923122037633478","positionID":"","phoneNum":"13688401095"},"travelType":0,"busiType":1,"isNeedFrequentTraveler":1,"allUserOrDeptUser":0}
		headers={
  'Content-Type': 'application/json;charset=UTF-8',
  'Host': api_data.Host,
  'la517_authSign': api_data.la517_authSign,
  'la517_clientInfo': api_data.la517_clientInfo,
  'la517_clientType': api_data.la517_clientType,
}
		response = requests.request("POST", url, headers=headers, data=json.dumps(data))
		print(response.text)
		if response.status_code==200:
			self.assertIn('Result',response.text)
			self.assertIn('成功', response.text)
		else:
			print('测试失败')
	def tearDown(self):
		pass
if __name__=='__main__':
	unittest.main()