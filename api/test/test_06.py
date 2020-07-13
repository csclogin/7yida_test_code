# -*- coding: utf-8 -*-
#  author caishicheng

import copy
# a=0
# sum=0
# b=1
# while sum<1000000:
#     sum=sum+a
#     a+=10
#     b+=1
#     if sum==1000:
#         break
# print(a)
# print(b)
# print(sum)

a=[1,2,[3]]
b=copy.copy(a)
c=copy.deepcopy(a)
b[2][0]=5
# c[0]=5
# c[2][0]=5
print(a)
