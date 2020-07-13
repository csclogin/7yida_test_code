# -*- coding: utf-8 -*-
#  author caishicheng
#createdate 2019-11-04
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
l=[1,2,3,4]
it=iter(l)
print(next(it))
print(next(it))
print(next(it))
print(111)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for i,j in knights.items():
    print(i,j)
