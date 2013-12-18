#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'CPyUG'
SITENAME = u'PyChina.org'
SITEURL = 'http://www.pychina.org'

MARKUP = ('rst', 'md', )
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Template settings: 
THEME = "_themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'readable'

DEFAULT_PAGINATION = 1
TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_CATEGORIES_ON_MENU = None      # 分类标签是否显示在导航

STATIC_PATHS = ['images', 'files'
    , 'extra/robots.txt'
    , 'extra/favicon.ico'
    ]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
    }


#   TIMEZONE = 'Europe/Paris'
TIMEZONE = u"Asia/Shanghai" #时区设置
DATE_FORMAT={"zh":("zh_CN","%Y-%m-%d,%a"),}  #日期格式设置，可按自己喜好设定
DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = u"feeds/all.rss.xml"
CATEGORY_FEED_RSS=u"feeds/%s.rss.xml"#为分类添加Feed
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'

# Plugins 
PLUGINS=['_plugins.sitemap', '_plugins.gzip_cache']
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

# Blogroll
LINKS =  None

# Social widget
ADDTHIS_PROFILE = True
DISQUS_SITENAME = u"{wwwpychinaorg}" #填入你的Shortname

#GITHUB_USER = "ZoomQuiet"

MENUITEMS = (('PyConChina', 'http://cn.pycon.org')
          ,('配置中可追加', '#')
          )

SOCIAL = (('github', 'https://github.com/PyConChina')
        , ('weibo', 'http://weibo.com/pyconcn')
        , ('O.B.P', 'http://weibo.com/openbookproject')
        , ('Wiki', 'http://wiki.woodpecker.org.cn/moin/CPUG')
        )

