#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os

AUTHOR = u'Andrew Becker'
SITENAME = u'Put Yourself Out There'
SITESUBTITLE = u"Reports from the front on Astrophysics, Statistics, and Data Science"
SITEURL = '' # change in publishconf.py

# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'

# Times and dates
#DEFAULT_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
TIMEZONE = 'US/Pacific'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Title menu options
MENUITEMS = [('Archives', '/archives.html'),
             ('Home Page', 'http://www.astro.washington.edu/users/becker')]
NEWEST_FIRST_ARCHIVES = True


## Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (#('<i class="icon-rss"></i> RSS', "%s/%s" % (FEED_DOMAIN, FEED_ATOM)),
          ('<i class="icon-github"></i> Github', 'http://www.github.com/acbecker'),
          ('<i class="icon-linkedin-sign"></i> LinkedIn', 'http://www.linkedin.com/in/acbecker'),
          ('<i class="icon-twitter"></i> Twitter', 'http://twitter.com/the__fog'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# intalled
#THEME = 'notmyidea'
# local
# https://github.com/duilio/pelican-octopress-theme.git
THEME = os.path.join(os.path.dirname(os.path.realpath(__file__)), "configuration/pelican-octopress-theme")

# very useful for debugging purposes
DELETE_OUTPUT_DIRECTORY = True

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# https://github.com/getpelican/pelican-plugins
PLUGIN_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "configuration/pelican-plugins")
PLUGINS = ['summary', 'latex', 'liquid_tags.img', 'liquid_tags.video', 'liquid_tags.include_code', 'liquid_tags.notebook', 'liquid_tags.literal']

# publishconf.py
## to get comments, etc
#DISQUS_SITENAME = "acbeckerblog" 
## GITHUB_URL = "https://github.com/acbecker" # Don't really want the "fork me" banner
#GOOGLE_ANALYTICS = "UA-42642734-1"

# Sharing
TWITTER_USER = 'the__fog'
GOOGLE_PLUS_USER = 'acbecker'
GOOGLE_PLUS_ONE = True
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = False
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'

# This header file is automatically generated by the notebook plugin
# Modified /astro/store/shared-scratch1/acbecker/LSST/lsst_devel/pelican-octopress-theme/templates/base.html
# to say
#  {% if EXTRA_HEADER %}
#    {{ EXTRA_HEADER }}
#  {% endif %}
# Not sure if this actually did anything tho...

# Actually, it appears to have included the EXTRA_HEADER again.  So
# let me just remove this from base.html, looks like this include
# functionality is already in there...
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found. "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER_1 = open('_nb_header.html').read().decode('utf-8')
    EXTRA_HEADER_2 = open('_table_header.html').read().decode('utf-8')
    EXTRA_HEADER = EXTRA_HEADER_1 + EXTRA_HEADER_2

# Trying to get the Category panel off the RHS, no effect.
CATEGORY_SAVE_AS = False

STATIC_PATHS = ['images', 'figures', 'downloads', 'favicon.png']
#STATIC_PATHS = [ 'extra/_config.yml', ]

EXTRA_PATH_METADATA = {
    'extra/_config.yml': {'path': '_config.yml'},
    }

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'
SEARCH_BOX = True

DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_CATEGORY = ""
