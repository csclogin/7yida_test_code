# -*- coding: utf-8 -*-
#  author caishicheng
import requests
import json

def login():
    url1='https://www.517la.com/login/loginVaildate'
    headers = {
  'Cookie': 'acw_tc=2760827815925563972233555e84546a497422421cc35e319b0a88f229d10b; '
            'JSESSIONID=C948713F1563A9F7803AE4D2E84C57E3; __wpkreporterwid_=7f30e867-4610-466a-a429-343cf38fbb90; '
            'qimo_seosource_34b2ea00-974c-11e9-84ff-034b0e5b1250=%E7%AB%99%E5%86%85; '
            'qimo_seokeywords_34b2ea00-974c-11e9-84ff-034b0e5b1250=; '
            'href=https%3A%2F%2Fwww.517la.com%2F; accessId=34b2ea00-974c-11e9-84ff-034b0e5b1250; '
            'pageViewNum=1; clbussuerName=; Hm_lvt_daffad6c1042cce8d8e763cad4e10d43=1592555626;'
            ' Hm_lpvt_daffad6c1042cce8d8e763cad4e10d43=1592556399; bad_id34b2ea00-974c-11e9-84ff-034b0e5b1250=64366e41-b209-11ea-b3d5-117c3bd14c24; '
            'nice_id34b2ea00-974c-11e9-84ff-034b0e5b1250=64366e42-b209-11ea-b3d5-117c3bd14c24; '
            'acw_tc=2760826415925569379082300e2792e1539adb2558e57ff9a68c4cf2438fee; '
            'cl_loginSign=ftD5V1wZxf8kdTJlohi%2FcQ%3D%3D; cl_loginKey=ftD5V1wZxf%2BQNjxuwiu1Rw%3D%3D; '
            'cl_loginKey1=uIH2QudNkFN2meVnvuW58%2BSPfov2mdFAA5lrMT4jDkGp15v35sW7jg%3D%3D; '
            'cl_loginKey2=vKU9qmGQv20Q3P6vlAy5li%2FkVQ7aV4Jg; cl_loginKey3=3u745qLLQO86rGQgcAVUAA%3D%3D',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}

    data= {'userName': '13688401095',
'passWord': '9689cc24bcc0c0ad3412e103ede17950f1369976df82bde085d93d0538e4667496f697a88584c335511bd6b22d8b749245421d252145274fef26c649734c4cc04314d826a3bf67cad4385f5c69451c74f4959992f7bbaa3ce880a0ab190786855208daceb511cfcefb2fa0dec3ae48a4c6523209915230fb1edb4c8ad1b30d37',
'phoneValidCode': '',
'validCode': '',
'loginType': '0'}

    response=requests.request("POST",url1,headers=headers,data=data)
    print(response.text)
    cookie1=response.cookies
    print(cookie1)
    return cookie1
login()
def login_entno():
    url="https://www.517la.com/Home/choseEntNo"
    data={'entNo': '20180316100422666114'}
    headers={
  'Cookie': 'acw_tc=2760827815925563972233555e84546a497422421cc35e319b0a88f229d10b; '
            'JSESSIONID=C948713F1563A9F7803AE4D2E84C57E3; __wpkreporterwid_=7f30e867-4610-466a-a429-343cf38fbb90; '
            'qimo_seosource_34b2ea00-974c-11e9-84ff-034b0e5b1250=%E7%AB%99%E5%86%85; '
            'qimo_seokeywords_34b2ea00-974c-11e9-84ff-034b0e5b1250=; '
            'href=https%3A%2F%2Fwww.517la.com%2F; accessId=34b2ea00-974c-11e9-84ff-034b0e5b1250; '
            'pageViewNum=1; clbussuerName=; Hm_lvt_daffad6c1042cce8d8e763cad4e10d43=1592555626;'
            ' Hm_lpvt_daffad6c1042cce8d8e763cad4e10d43=1592556399; bad_id34b2ea00-974c-11e9-84ff-034b0e5b1250=64366e41-b209-11ea-b3d5-117c3bd14c24; '
            'nice_id34b2ea00-974c-11e9-84ff-034b0e5b1250=64366e42-b209-11ea-b3d5-117c3bd14c24; '
            'acw_tc=2760826415925569379082300e2792e1539adb2558e57ff9a68c4cf2438fee; '
            'cl_loginSign=ftD5V1wZxf8kdTJlohi%2FcQ%3D%3D; cl_loginKey=ftD5V1wZxf%2BQNjxuwiu1Rw%3D%3D; '
            'cl_loginKey1=uIH2QudNkFN2meVnvuW58%2BSPfov2mdFAA5lrMT4jDkGp15v35sW7jg%3D%3D; '
            'cl_loginKey2=vKU9qmGQv20Q3P6vlAy5li%2FkVQ7aV4Jg; cl_loginKey3=3u745qLLQO86rGQgcAVUAA%3D%3D',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
    print(headers)
    response = requests.request("POST", url, headers=headers, data=data)
    print(response.text)

# login_entno()

def get_auth():
    url = "https://www.517la.com/Home/getAuthSignByUserNoForCloud"
    data = {}
    headers = {
        'Cookie': 'acw_tc=2760827815925563972233555e84546a497422421cc35e319b0a88f229d10b; '
                  'JSESSIONID=C948713F1563A9F7803AE4D2E84C57E3; __wpkreporterwid_=7f30e867-4610-466a-a429-343cf38fbb90; '
                  'qimo_seosource_34b2ea00-974c-11e9-84ff-034b0e5b1250=%E7%AB%99%E5%86%85; '
                  'qimo_seokeywords_34b2ea00-974c-11e9-84ff-034b0e5b1250=; '
                  'href=https%3A%2F%2Fwww.517la.com%2F; accessId=34b2ea00-974c-11e9-84ff-034b0e5b1250; '
                  'pageViewNum=1; clbussuerName=; Hm_lvt_daffad6c1042cce8d8e763cad4e10d43=1592555626;'
                  ' Hm_lpvt_daffad6c1042cce8d8e763cad4e10d43=1592556399; bad_id34b2ea00-974c-11e9-84ff-034b0e5b1250=64366e41-b209-11ea-b3d5-117c3bd14c24; '
                  'nice_id34b2ea00-974c-11e9-84ff-034b0e5b1250=64366e42-b209-11ea-b3d5-117c3bd14c24; '
                  'acw_tc=2760826415925569379082300e2792e1539adb2558e57ff9a68c4cf2438fee; '
                  'cl_loginSign=ftD5V1wZxf8kdTJlohi%2FcQ%3D%3D; cl_loginKey=ftD5V1wZxf%2BQNjxuwiu1Rw%3D%3D; '
                  'cl_loginKey1=uIH2QudNkFN2meVnvuW58%2BSPfov2mdFAA5lrMT4jDkGp15v35sW7jg%3D%3D; '
                  'cl_loginKey2=vKU9qmGQv20Q3P6vlAy5li%2FkVQ7aV4Jg; cl_loginKey3=3u745qLLQO86rGQgcAVUAA%3D%3D',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    response = requests.request("POST", url, headers=headers, data=data)
    print(response.text)
    return response.text
get_auth()