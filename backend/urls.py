#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: vv
# Date: 2019/8/26

from .views import *
from django.conf.urls import url


api_urlpatterns = [
    url(r'api/user/login', login, name="user_login"),
    url(r'api/user/logut', logout, name="user_logout"),
]