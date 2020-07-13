# -*- coding: utf-8 -*-
#  author caishicheng

def w1(fun):
    print("装饰器开始修饰")
    def inner():
        print("验证权限")
        fun()
    return inner

@w1
def test():
    print("test")
test()

# def F1(fun):
#     print(1)
#     def inner():
#         print(2)
#         fun()
#     return inner
# @F1
# def test():
#     print("test")
# test()

