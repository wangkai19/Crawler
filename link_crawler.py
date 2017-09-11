# -*- coding:UTF-8 -*-
import urllib2
import re
import urlparse

#use urllib2 download html by a url
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

#Return a list of lists from html
def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return webpage_regex.findall(html)

def link_crawler(seed_url,link_regex):
    crawl_queue = [seed_url]
    #keep track which URL's have seen before
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex,link):
                #be absolute link
                link = urlparse.urljoin(seed_url,link)
                #check if have alreadly seen this link
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)

link_crawler('http://example.webscraping.com','/(places/default/view|places/default/index)')