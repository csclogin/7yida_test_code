# -*- coding: utf-8 -*-
#  author caishicheng
def f1(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return f1(n-2)+f1(n-1)


print(f1(10))