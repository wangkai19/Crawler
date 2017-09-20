#-*- coding:UTF-8 -*-
from link_crawler import download
import re
import lxml.html

url = 'http://example.webscraping.com/places/default/view/Armenia-12'
html = download(url)

#利用正则表达式抓取了数据
#print re.findall('',html)[1]

#利用lxml的CSS选择器来抓取数据
tree = lxml.html.fromstring(html)
td = tree.cssselect('tr#places_area_row > td.w2p_fw')[0]
print td.text_content