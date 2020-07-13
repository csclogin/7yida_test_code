# -*- coding: utf-8 -*-
#  author caishicheng


import os
import time
import shutil

# a= os.popen("dir")
# print(a.read())


# os.system()
# path="G:\\"
# f=open(r'G:\test\dir.txt','w')
# for root,dirs,files in os.walk(path):
#     for dir in dirs:
#         for file in files:
#             f.write(file)
#             f.write('\n')
# f.close()
##找出G盘下，badboy.exe的文件个数
f=open(r'G:\test\dir.txt','r')
a=0
for line in f.readlines():
    if 'badboy.exe'  in line:
        a+=1
print(a)



# a=time.time()
# print(a)
# print(a.__class__)
# b=time.localtime()
# print(b)
# now_year=time.strftime('%Y%m%d')
# print(now_year)

# file="G:\\ReadMe.txt"
# with open(file,'r') as f:
#     line=f.readlines()
#     print(line)
# l=open("G:\\ReadMe.txt",'w')
# l.write("asasa")
# print(l.readlines())


# shutil.copy(r'G:\test\aaa.txt',r'G:\test2')

