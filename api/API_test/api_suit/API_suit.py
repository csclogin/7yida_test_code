# -*- coding: utf-8 -*-
#  author caishicheng
from API_test.common.HTMLTestRunner import HTMLTestRunner
import unittest,os,time

t1= queryHotelListNew.Hotel_queryHotelListNew('test_queryHotelListNew')
t2= queryHotelPriceInfo.Hotel_queryHotelPriceInfo('test_queryHotelPriceInfo')
t3= preCreateOrder.Hotel_preCreateOrder('test_preCreateOrder')
t4= createOrder.Hotel_createOrder('test_createOrder')

suite=unittest.TestSuite()
suite.addTests([t1,t2,t3,t4])
project_path=os.path.dirname(os.getcwd())
testport_path=project_path+"\\testport\\"+time.strftime("%Y%m%d%H%M%S")+'.html'
print(testport_path)
fp=open(testport_path,'wb')
runner=HTMLTestRunner(stream=fp,title='接口自动化测试报告',description='')
runner.run(suite)