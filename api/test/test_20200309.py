import os
import random
str='Runboot'
# print(str)
# print(str+'   hello')
# l=[]
# for i in str:
#     l.append(i)
# print(l)
# print(len(l))
# a='sahdjkaslhdjsakdhbsajkdlhbsajdas'
# c=a.find('as')
# d=a.index('jdas')
# print(c)
# print(d)
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# # for i in knights:
# #     print(i)
# #     print(knights[i])

# project_path=os.path.dirname(os.getcwd())
# print(project_path)

# def fib(n):
#     a=0
#     b=1
#     for i in range(0,n):
#         print(b)
#         a,b=b,a+b
# fib(20)

# if __name__=='__main__':
#     print(1)
# else:
#     print(0)


# b=random.randint(0,10)
# print(b)
# while True:
#     a = int(input('请输入数字'))
#     if a>10:
#         print('请输入0-10')
#     if a==b:
#         print('厉害啦')
#         break
#     elif a<b:
#         print('小了')
#     else:
#         print('大了')


for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d' %(i,j,i*j),end='\t')
    print('')


# print('{},{}'.format(1,2))

