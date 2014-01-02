#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
###############################################################
###############################################################   Site abt.
###############################################################
AUTHOR = u'CPyUG'
SITENAME = u'PyChina.org'
SITEURL = 'http://pychina.org'
DISQUS_SITENAME = u"pychinaorg" #填入你的Shortname

MARKUP = ('md', )#'rst', 'html', 
#   TIMEZONE = 'Europe/Paris'
TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
        'zh_CN': '%Y-%m-%d %H:%M',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'
DEFAULT_DATE = 'fs' # use filesystem's mtime

#LOCALE = ('zh_CN.utf8',)
DEFAULT_LANG = u'zh_CN'
FILENAME_METADATA = '(?P<slug>.*)'

###############################################################
###############################################################   Plugins abt.
###############################################################
# Plugins 
PLUGINS=['_plugins.sitemap'
    #, '_plugins.gzip_cache'
    ]
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
###############################################################
###############################################################   Template abt.
###############################################################
THEME = "_themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'readable'

DEFAULT_PAGINATION = 1
TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_CATEGORIES_ON_MENU = None      # 分类标签是否显示在导航
# Social widget
ADDTHIS_PROFILE = True

#GITHUB_USER = "ZoomQuiet"
MENUITEMS = (('PyConChina', 'http://cn.pycon.org')
          ,('News', 'http://news.pychina.org')
          )

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_RSS= None
SOCIAL = (('GitHub', 'https://github.com/PyConChina')
        , ('Weekly', 'http://weekly.pychina.org')
        , ('News', 'http://news.pychina.org')
        , ('rss', SITEURL + '/' + FEED_ALL_ATOM)
        , ('CPyUG', 'https://gitcafe.com/CPyUG')
        , ('Wiki', 'http://wiki.woodpecker.org.cn/moin/CPUG')
        , ('weibo', 'http://weibo.com/pyconcn')
        , ('O.B.P', 'http://weibo.com/openbookproject')
        )
# Blogroll
LINKS =  None
###############################################################
###############################################################   Publish abt.
###############################################################
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = None  #!!! for .github.io can not clean outupt/.git
DEFAULT_CATEGORY = u'Chaos'

TEMPLATE_PAGES = {
        "404.html": "404.html",
        }

STATIC_PATHS = ['_images', '_files'
    , '_extra/robots.txt'
    , '_extra/favicon.ico'
    , '_extra/README.md'
    ]

EXTRA_PATH_METADATA = { '_extra/favicon.ico': {'path': 'favicon.ico'}
    ,'_extra/robots.txt': {'path': 'robots.txt'}
    , '_extra/README.md': {'path': 'README.md'},
    }

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True





