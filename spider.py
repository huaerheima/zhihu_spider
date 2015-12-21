#!/usr/bin/env python
# coding:utf-8
import re
import sys
import json
import uniout
import getopt
import logging
import urllib2
import webbrowser
from pyh import *

URL = "http://news-at.zhihu.com/api/4/news/"
PATH_HTML = "/Users/wangyujie/Desktop/1.html"
PATH_TXT = "/Users/wangyujie/Desktop/1.txt"
logger = logging.getLogger(__name__)
Header = ""

def get_news_latest():
    try:
        response = urllib2.urlopen(URL+"latest")
        content = response.read()
    except urllib2.URLError:
        logger.error('哎哟,好像出错了')
        return
    return content

def get_stories_to_news(content):
    dict_content = json.loads(content)
    for i in range(len(dict_content['stories'])):
        try:
            response = urllib2.urlopen(URL+str(dict_content['stories'][i]["id"]))
            dict_content['stories'][i].setdefault("body", json.loads(response.read())["body"])
        except urllib2.URLError:
            logger.error('哎哟,好像出错了')
            return
    return json.dumps(dict_content)

def add_news_to_html(content):
    html_content = ''
    with open(PATH_TXT,"r") as f:
        html_content = f.read()
    with open(PATH_HTML,"w") as ff:
        ff.write(html_content.replace("zhihuribao",str(content)))


if __name__=="__main__":
    news_latest = get_news_latest()
    news_latest = get_stories_to_news(news_latest)
    add_news_to_html(news_latest)
    print news_latest
    webbrowser.open_new_tab("file:///Users/wangyujie/Desktop/1.html")


