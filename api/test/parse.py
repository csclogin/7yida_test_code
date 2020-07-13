import  requests
import re
import time

# def parse_1():
#     url="https://www.baidu.com"
#     for i in range(20):
#         parse_2(url)
# def parse_2(url):
#     response=requests.get(url)
#     print(response.status_code)
#
#
# parse_1()




# 获取章节信息和url
def get_chapter_list():
    response = requests.get('http://www.jinyongwang.com/tian/')
    response.encoding = 'utf-8'
    html = response.text
    print(html)
    div = re.findall(r'</a></li><li><a href="/tian/.*?</a></li><li><a href="/tian/645.html')[0]
    print(div)
    chapter_list = re.findall(r'<a href="(.*?)" title=".*?">(.*?)</a>', div)
    return chapter_list


# 获取章节内容
def chapter_download(chapter_url):
    chapter_dl = requests.get(chapter_url)
    chapter_dl.encoding = 'utf-8'
    chapter_html = chapter_dl.text
    chapter_content_download = re.findall(r'id=\"content\">(.*?)<div class=\"backs\">', chapter_html, re.S)[0]

    # 清洗数据
    chapter_content_download = chapter_content_download.replace(' ', '')
    chapter_content_download = chapter_content_download.replace(' ', '')
    chapter_content_download = chapter_content_download.replace('<br/>', '')
    chapter_content_download = chapter_content_download.replace(
        '<!--<divstyle="margin:1px1px6px1px;"><scriptsrc=/d/js/acmsd/thea16.js></script></div>-->', '')
    return chapter_content_download


# 循环章节，建立章节文本存取小说内容
for chapter_url, chapter_title in get_chapter_list():
    chapter_url = 'http://www.xs4.cc%s' % chapter_url
    print(chapter_url, chapter_title)

    # 数据持久化
    print('正在保存 %s' % chapter_title)
    fn = open('%s.text' % chapter_title, 'a+', encoding='utf-8')
    fn.write(chapter_download(chapter_url))

