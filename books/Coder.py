#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__  = 'JingkaiTang'
__version__ = '0.1'

from base import BaseFeedBook


def getBook():
    return Coder


class Coder(BaseFeedBook):
    title = u'Coder News'
    __author__ = 'calibre'
    description = u'程序员资讯订阅'
    language = 'zh-cn'
    feed_encoding = 'utf-8'
    page_encoding = 'utf-8'
    mastheadfile = 'mh_default.gif'
    coverfile = 'cv_default.jpg'
    network_timeout = 60
    oldest_article = 7
    max_articles_per_feed = 9
    deliver_days = []
    deliver_times = [8, 20]
    oldest_article = 1
    feeds = [
        (u'开源中国', 'http://www.oschina.net/news/rss'),
        (u'Engadget', 'https://www.engadget.com/rss.xml'),
    ]


