# -*- coding: utf-8 -*-
#  author caishicheng

import random
import pymysql
import os

#姓名列表wori1
xm_list=["何","吕","施","张","孔","曹","严","华","金","魏","陶","姜","戚","谢","邹","喻","柏","水","窦","章"
"云","苏","潘","葛","奚","范","彭","郎","鲁","韦","昌","马","苗","凤","花","方","俞","任","袁","柳"
"酆","鲍","史","唐","费","廉","岑","薛","雷","贺","倪","汤","滕","殷","罗","毕","郝","邬","安","常"
"乐","于","时","傅","皮","卞","齐","康","伍","余","元","卜","顾","孟","平","黄","和","穆","萧","尹"
"姚","邵","湛","汪","祁","毛","禹","狄","米","贝","明","臧","计","伏","成","戴","谈","宋","茅","庞"
"熊","纪","舒","屈","项","祝","董","粱","杜","阮","蓝","闵","席","季","麻","强","贾","路","娄","危"
"江","童","颜","郭","梅","盛","林","刁","钟","徐","邱","骆","高","夏","蔡","田","樊","胡","凌","霍"
"虞","万","支","柯","昝","管","卢","莫","经","房","裘","缪","干","解","应","宗","丁","宣","贲","邓"
"郁","单","杭","洪","包","诸","左","石","崔","吉","钮","龚","程","嵇","邢","滑","裴","陆","荣","翁"
"荀","羊","於","惠","甄","麴","家","封","芮","羿","储","靳","汲","邴","糜","松","井","段","富","巫"
"乌","焦","巴","弓","牧","隗","山","谷","车","侯","宓","蓬","全","郗","班","仰","秋","仲","伊","宫"
"宁","仇","栾","暴","甘","钭","厉","戎","祖","武","符","刘","景","詹","束","龙","叶","幸","司","韶"
"郜","黎","蓟","薄","印","宿","白","怀","蒲","邰","从","鄂","索","咸","籍","赖","卓","蔺","屠","蒙"
"池","乔","阴","欎","胥","能","苍","双","闻","莘","党","翟","谭","贡","劳","逄","姬","申","扶","堵"
"冉","宰","郦","雍","舄","璩","桑","桂","濮","牛","寿","通","边","扈","燕","冀","郏","浦","尚","农"
"温","别","庄","晏","柴","瞿","阎","充","慕","连","茹","习","宦","艾","鱼","容","向","古","易","慎"
"戈","廖","庾","终","暨","居","衡","步","都","耿","满","弘","匡","国","文","寇","广","禄","阙","东"]

#年龄列表
nl_list=[]
for i in range(10,20):
    nl_list.append(i)

#性别列表
xb_list=['M','F']

#班级列表
bj_list=[]
for i in range(20):
    bj_list.append(i)

# with open(r"G:\sql.txt",'a+') as f:
    # f.write("insert into test.xsb(xm,nl,xb,bj) value")
    # sql="insert into test.xsb(xm,nl,xb,bj) value"

# def execute_sql():
#     xm=random.choice(xm_list) + random.choice(xm_list)
#     nl=random.choice(nl_list)
#     xb=random.choice(xb_list)
#     bj=random.choice(bj_list)
#
#     db=pymysql.connect()
#     cursor = db.cursor()
#     sql="insert into test.xsb(xm,nl,xb,bj) value(\'%s\',\'%s\',\'%s\',\'%s\')" %(xm,nl,xb,bj)+';'
#     cursor.execute(sql)
#     db.commit()
#     sql="select count(*) from test.xsb;"
#     # sql="show databases;"
#     cursor.execute(sql)
#     data = cursor.fetchall()
#     print(data)
#     db.close()
# for i in range(1):
#     execute_sql()




for i in range(1,11):
    for j in range(1,7):
        cj=random.randint(50,100)
        db = pymysql.connect()
        cursor = db.cursor()
        # sql="insert into test.xsb(xm,nl,xb,bj) value(\'%s\',\'%s\',\'%s\',\'%s\')" %(xm,nl,xb,bj)+';'
        sql = "insert into test.cjb(id,kch,cj) value(\'%s\',\'%s\',\'%s\')" %(i,j,cj) + ';'
        cursor.execute(sql)
        db.commit()
    # f=open(r"g:\sql.txt",'a+')
    # f.write(sql)
    # f.write('\n')
    # f.close()