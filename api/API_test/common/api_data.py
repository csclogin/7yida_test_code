# -*- coding: utf-8 -*-
#  author caishicheng
import re
import requests,json,time
from API_test.common import method_get_data


checkInDate= "2020-08-21"
checkOutDate="2020-08-22"
la517_authSign='6363E03F0061B03A7D90DA4D3E8559443A5D1434D5F185E8858EE262C185BE4EE0D798465454EC187480E27AA78A238711BBC8452925CA7FAF66759EBDDF1158'
la517_clientInfo='eyJwa2duYW1lIjoiY29tLm5hNTE3LkNMQWlyVGlja2V0SDUiLCJjbGllbnR0eXBlIjozLCJtY29kZSI6IiIsInRpbWVzdGFtcCI6IjIwMjAtMDYtMTcgMTU6MjI6MDUiLCJ2ZXJzaW9uIjoiODIzNCJ9'
ratePlanID=''
ChannelID=''
hotelID=''
RoomID=''
personOrCompay='2'
la517_clientType='201'
Host='jpgatewaycs.517la.com'
Host1='restfulcs_jk.517la.com'
now_day=time.strftime('%Y')+'-'+time.strftime('%m')+'-'+time.strftime('%d')


