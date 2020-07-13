# -*- coding: utf-8 -*-
#  author caishicheng


# -*- coding: utf-8 -*-
#  author caishicheng


import requests
import unittest
import json
from API_test.common import api_data,method_get_data
import time


class Hotel_preCreateOrder(unittest.TestCase):
	def setUp(self):
		print('开始测试')
	def test_preCreateOrder(self):
		url="https://www.517la.com/Home/getAuthSignByUserNoForCloud"
		data={}
		headers={
  '__wpkreporterwid_': '65151c00-8b1d-45bb-3d77-c509222ea3f8',
  'accessId': '34b2ea00-974c-11e9-84ff-034b0e5b1250',
  'acw_tc': '2760828915903958836203813e2914fd8d895526758c698ddd3df962c91e08',
  'bad_id34b2ea00-974c-11e9-84ff-034b0e5b1250': '190c8a71-9a68-11ea-b3d5-117c3bd14c24',
  'cl_entno': '20180316100422666114',
  'cl_loginKey': 'ftD5V1wZxf%2BQNjxuwiu1Rw%3D%3D',
  'cl_loginKey1': 'uIH2QudNkFN2meVnvuW58%2BSPfov2mdFAA5lrMT4jDkGp15v35sW7jg%3D%3D',
  'cl_loginKey2': 'vKU9qmGQv20Q3P6vlAy5li%2FkVQ7aV4Jg',
  'cl_loginKey3': 'jnhYfWr0rkCubs0njOFVrw%3D%3D',
  'cl_loginSign': 'ftD5V1wZxf8kdTJlohi%2FcQ%3D%3D',
  'cl_loginKey3': 'jnhYfWr0rkCubs0njOFVrw%3D%3D',
  'cl_loginSign': 'ftD5V1wZxf8kdTJlohi%2FcQ%3D%3D',
  'cl_sid': 'ea7b28ae-4beb-4a8d-83bf-4c82780e3e142',
  'cl_uk': 'c6Z%2BFT5ewdH9xM4K4vxFkmb%2Foexuo0xLOG75ZUg5%2FCKFoe1ninqTW7%2FDmWZhX5dcvBXcn2gVJNQ3%0A0vOKxvSgbwFvaxaRAm94cVNg%2FQq8Bketg8r9QyQJom1s%2FDN0S%2Frm9NkHHy2%2BLSdfw78LHt7TR2iZ%0AF1jpcuYPxGie8TCzwrkD4%2BLAbjykO74TypjE3OyxBdKShHsaI%2F9Yz2jW%2FD4YT%2BwCbzPOg1cw49%2FH%0A84BcY2OE9hqT48vZbSB78eW16QL%2BHuyS2BiK8BovLCroROFsbdVqkfXVLmDNXSmRT%2BzEU246%2B7fG%0A3vO5DRi%2FY83T%2BDxUF%2BW6nf9Xo3OUkEeYnHY3NKKGx1ng%2BCDdZv51id8bX5isLsKQEgLoHBo1pRnb%0A6kxXdeYTpvOXR3lKaZu3%2FsfK9%2Fiz12WvEbzlKja46%2FwJrntSgTab%2FrXgENHb2I4QIy%2Fgt5OAdoKy%0AT968gg7qWmn2axGoJRINDcBmDOmfg3AuPAYBQF%2FLeBnH2y17IvXdCNd3qdeb9%2BbFu44%3D',
  'clbussuerName': '',
  'CLBussUserWeb': '0',
  'CLBussUserWebFirst': '01',
  'CookieUser': 'undefined',
  'DH_LIMITVOYAGE': '',
  'DH_MAINAPPLYID': '',
  'entNo': '20180316100422666114',
  'Hm_lpvt_daffad6c1042cce8d8e763cad4e10d43': '1590396183',
  'Hm_lvt_daffad6c1042cce8d8e763cad4e10d43': '1589958397',
  'href': 'https%3A%2F%2Fwww.517la.com%2F',
  'JSESSIONID': '168834BEDF692AFA99BADFC4581FA978',
  'nice_id34b2ea00-974c-11e9-84ff-034b0e5b1250': '190c8a72-9a68-11ea-b3d5-117c3bd14c24',
  'pageViewNum': '19',
  'qimo_seokeywords_34b2ea00-974c-11e9-84ff-034b0e5b1250': '',
  'qimo_seosource_34b2ea00-974c-11e9-84ff-034b0e5b1250': '%E7%AB%99%E5%86%85',
  'RETURNHOME_URL': 'www.517la.com%2F',
  'sessionID': '245fcad2-2589-4559-8716-e354bdf001652',
  'u': '{"sessionID":"ea7b28ae-4beb-4a8d-83bf-4c82780e3e142","entNo":"20180316100422666114","tmcNo":"20160512144219375328","userNo":"20190923122037633478","staffNo":"20190923134348848187","url":"stcs_m.517la.com","userName":"%E8%94%A1%E4%B8%96%E6%88%90"}',
  'Cookie': 'acw_tc=2760827115903967619423339ef869d191cbba68c4479a60ff2cf86713f876; JSESSIONID=F367C4868B19CD229E3DA3A9A32F9FA6'
}
		response = requests.request("POST", url, headers=headers, data=data)
		print(response.text)
		if response.status_code==200:
			self.assertIn('成功',response.text)
			self.assertIn('PreBookResult\\":1', response.text)
		else:
			print('测试失败')
	def tearDown(self):
		pass
if __name__=='__main__':
	unittest.main()