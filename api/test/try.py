# -*- coding: utf-8 -*-
#  author caishicheng
import  time
import re

# try:
#     raise RuntimeError("testerror")
#     # "a"+"b"
# # except TypeError as e:
# #     print(e)
# except:
#     print("失败后打印")
# else:
#     print("没有异常执行")
# finally:
#     print("最后都要执行")
#
#

# a=time.time()
# print(a)
# b=time
#
# print(b)
# def showplus(x):
#     print(x)
#     return x + 1
# num = showplus(6)
# print(num)
# add = num + 2
# print(add)


a=['\\":\\"0010010011608230019052539183vF03655\\",\\"']
b=re.findall(r'00(.+?)',a)
print(b)