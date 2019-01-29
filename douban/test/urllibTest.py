# -*- coding: utf-8 -*-
from urllib import request
from urllib.request import Request
from urllib import parse


def getNormal():
    response = request.urlopen("http://www.baidu.com")
    print(response.read().decode("utf-8"))


# 设置请求头
def getWithUserAgent():
    req = request.Request("http://www.baidu.com")
    req.add_header("User-Agent",
                   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)")
    response = request.urlopen(req)
    print(response.read().decode("utf-8"))


def postNormal():
    req = Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")
    postData = parse.urlencode([
        ("key1", "val1"), ("key2", "val2"), ("keys", "val3")
    ])

    req.add_header("Origin", "http://www.thsrc.com.tw")
    req.add_header("User-Agent",
                   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)")
    response = request.urlopen(req, data=postData.encode("utf-8"))
    print(response.read().decode("utf-8"))


getWithUserAgent()
