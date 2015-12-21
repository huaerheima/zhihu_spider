# zhihu_spider
#爬取知乎日报（app）内容到本地页面并打开

*import re
*import sys
*import json
*import uniout
*import getopt
*import logging
*import urllib2
*import webbrowser

#把page.txt 页面放到桌面上，mac下的路径为"/Users/wangyujie/Desktop/page.txt"
#在终端运行spider.py文件，就会在桌面生成"/Users/wangyujie/Desktop/spider.html"页面并打开
