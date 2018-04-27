# coding=utf-8
import requests
import urllib2
import os

from lxml import etree
# html = urllib2.Request("http://cl.d5j.biz/htm_mob/7/1612/2172569.html")
# html.encoding = 'utf-8'
# selector = etree.HTML(html.text)
# content = selector.xpath('//table//img/@src')
for each in range(0,98):
    # 图片路径及名称
    imgurl = "http://www.17sucai.com/preview/499951/2016-06-22/wexinbiaoqing/images/arclist/"
    name = str(each) + ".gif"

    # 切换到图片存储目录
    os.chdir(r"C:\Users\dell\OneDrive\pythonWorkspace\douyu\Images")

    a
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
        'Cookie': 'AspxAutoDetectCookieSupport=1',
    }
    request = urllib2.Request(imgurl+name, None, header)  #刻意增加头部header，否则本行与下一行可以写为：response = urllib2.urlopen(imgurl)
    response = urllib2.urlopen(request)
    f = open(name, 'wb')
    f.write(response.read())
    f.close()
    print(imgurl+name)
