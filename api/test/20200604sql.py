# -*- coding: utf-8 -*-
#  author caishicheng
import pymysql
from random import choice




def insert_cjb():
    id_list = [1, 2, 3, 4, 5, 6]
    kch_list = ['1', '2', '3', '4', '5', '6']
    cj_list = []
    for i in range(0, 101):
        cj_list.append(i)
        cj=choice(cj_list)
    db=pymysql.connect()
    cursor=db.cursor()
    sql="insert into test.cjb value('%d','%d','%f')" %(id,kch,cj)+";"
    cursor.execute(sql)
    db.commit()
for id in range(1,7):
    for kch in range(1,7):
      insert_cjb()