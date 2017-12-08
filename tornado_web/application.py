#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import urls
import os

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__),"templates"),
    static_path = os.path.join(os.path.dirname(__file__),"statics"),
    debug = True,
)
application = tornado.web.Application(
    handlers= urls.url,
    **settings
)