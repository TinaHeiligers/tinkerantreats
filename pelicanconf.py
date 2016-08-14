#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tina H'
SITENAME = u'Tinker an Treats'
SITEURL = ''
# GITHUB_URL = 'http://github.com/TinaHeiligers/'
PATH = 'content'

TIMEZONE = 'America/Phoenix'

DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 4
REVERSE_CATEGORY_ORDER = True

DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/tinaheiligers1'),
          ('LinkedIn', 'https://www.linkedin.com/in/christianeheiligers'),)

SUMMARY_MAX_LENGTH = 20

STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {
  'extra/CNAME':{'path':'CNAME'}
}
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

