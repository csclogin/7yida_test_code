# -*- coding: utf-8 -*-
#  author caishicheng


import requests
import unittest
import json
from API_test.common import api_data,method_get_data
import time


class Hotel_createOrder(unittest.TestCase):
	def setUp(self):
		print('开始测试')
	def test_createOrder(self):
		url=r'https://'+api_data.Host+r"/h5/HOTELSELLINTERFACEWEB/api/createOrder"
		data={
	"orderUserExtraInfoDetail": [],
	"personCostCenterList": [{
		"staffNo": "20190923134348848187",
		"staffName": "蔡世成",
		"deptCostCenterIDs": "1911210931381360914vI08502",
		"deptCostCenterNums": "SJ",
		"deptCostCenterNames": "设计",
		"deptSubjectCodes": "0002",
		"deptSubjectNames": "测试2",
		"deptCostCenterRatios": 100,
		"deptCostCenterPrices": method_get_data.get_AveragePrice()
	}],
	"personCostCenterListM": [{
		"index": 0,
		"costCenterID": "1911210931381360914vI08502",
		"costCenterType": 1,
		"costCenterNo": "SJ",
		"costCenterName": "设计",
		"staffList": [{
			"staffNo": "20190923134348848187",
			"staffName": "蔡世成",
			"isFit": 1
		}],
		"subjectCode": "0002",
		"subjectName": "测试2",
		"costPercent": 100,
		"costMoney": method_get_data.get_AveragePrice(),
		"selectedStaffList": "蔡世成"
	}],
	"orderApplyRelation": [{
		"staffNO": "20190923134348848187",
		"staffName": "蔡世成",
		"applyNO": "",
		"mainApplyNO": "",
		"isIllegal": 4,
		"applyReason": "",
		"illegalContent": "",
		"illegalReason": "",
		"actualStandard": "",
		"passengerTypeID": 0,
		"passengerCertTypeID": 0,
		"passengerCertNum": "",
		"passengerGender": 1,
		"passengerBirth": "1900-01-01",
		"passengerPositionId": "",
		"passengerDeptId": "20180316100422666114",
		"passengerDeptName": "思存测试企业",
		"passengerPhone": "",
		"userNo": "20190923122037633478",
		"outStaffNo": "",
		"CompanyAdvFee":method_get_data.get_AveragePrice(),
		"PersonPayFee": 0,
		"standardPrice": 0,
		"departmentNO": "20180316100422666114",
		"personRoomFee": 17
	}],
	"hotelCode": method_get_data.get_HotelID(),
	"hotelName": "北京蜡笔小新青年公寓",
	"countryName": "中国",
	"provinceName": "北京",
	"hotelBaiduLongitude": "116.471376",
	"hotelBaiduLatitude": "39.896395",
	"hotelPhone": "17701139812",
	"roomTypeID":method_get_data.get_RoomID(),
	"ratePlanID": method_get_data.get_RatePlanID(),
	"contractName": "子骥",
	"contractStaffID": "20190923134348848187",
	"contractTel": "13688401095",
	"guestCount": 1,
	"roomNum": 1,
	"handlFee": 0,
	"tmcFee": 0,
	"technologyServiceFee": 0,
	"invoiceAppendFee": 0,
	"totalPrice": method_get_data.get_AveragePrice(),
	"checkInDate": api_data.checkInDate,
	"checkOutDate": api_data.checkOutDate,
	"days": 1,
	"currencyCode": "CNY",
	"adultCount": 1,
	"childCount": 0,
	"childAges": [],
	"latestArrivalTime": api_data.checkOutDate+" 23:59:59",
	"checkInType": "2",
	"sellPlat": 4,
	"cityID": "001001001",
	"roomName": "标准间",
	"staffAccount": "",
	"sellChannel": 1,
	"productType": 1,
	"invoiceType": 0,
	"roomFacilities": "",
	"orderFlag": "0000000",
	"buyChannelInfo": {'channel':method_get_data.get_ChannelID()} ,
	"cityName": "北京",
	"travelGoal": "1",
	"hotelAddress": "双井百环家园5号楼",
	"guestInfoList": [{
		"personName": "蔡世成",
		"personType": 1,
		"isSeniorExecutive": 0,
		"cardType": 0,
		"phone": "",
		"cardID": "513***********7578",
		"isOver": 0,
		"roomPersonType": 1,
		"staffNO": "20190923134348848187"
	}],
	"remark": "",
	"CompanyAdvFee": 0,
	"PersonPayFee": 0,
	"CompanyPayStatus": -1,
	"PersonPayStatus": -1,
	"hotelSellCancelRuleList": [],
	"roomNightPriceList": [],
	"isAgentBook": 0,
	"serviceStatus": 1,
	"orderType": 0
}
		headers={
  'Content-Type': 'application/raw;charset=UTF-8',
	'auth':api_data.la517_authSign,
  'la517_authSign': api_data.la517_authSign,
  'la517_clientInfo': api_data.la517_clientInfo,
  'la517_clientType': api_data.la517_clientType,
}
		response = requests.request("POST", url, headers=headers, data=json.dumps(data).encode())
		print(response.text)
		if response.status_code==200:
			self.assertIn('成功',response.text)
			self.assertIn('PreBookResult\\":1', response.text)
		else:
			print('测试失败')
	def tearDown(self):
		pass
if __name__=='__main__':
	unittest.main()