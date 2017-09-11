# -*- coding:UTF-8 -*-
import urllib2

def download(url,user_agent = 'QiaoBa',num_retries = 2):
    print 'Downloading:',url
    headers = {'User_agent':user_agent}
    requests = urllib2.Request(url,headers = headers)
    try:
        html = urllib2.urlopen(requests).read()
    except urllib2.URLError as e:
        print 'Download error',e.reason
        html = None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code < 600:
                return download(url,user_agent,num_retries - 1)
    return html

print download('http://example.webscraping.com')