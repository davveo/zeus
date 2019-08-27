#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: vv
# Date: 2019/8/23

from django.conf.urls import url

from .views import *

order_url_patterns = [
    url(r'order/', test, name="test")
]