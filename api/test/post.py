# -*- coding: utf-8 -*-
#  author caishicheng



import requests

url = "http://ptcs.hotel.517na.com/Login/LoginAjax"

payload={"userID":"13688401095","pwd":"78ba7c277f7bcaebeab13e4a715e0d84bf365284a719ef31cc0eb76da239bb03880a28479f7a6ccd8"
                                      "1dc84c528e63f98ff5d418793fa5473c4d52959e538b2d845c01a7c8088a4503cff48b9ffba3ec1b1"
                                      "b1b2cdb24212ca6d87533af1b08425f156c8ad530da3d576a6f10b173c498aa72d3e6edbf14f52d7"
                                      "7fb328db825411","validateCode":"62md"}


response = requests.request("POST", url, data=payload)

print(response.text)
print(response.headers)