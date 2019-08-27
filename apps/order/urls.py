#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: vv
# Date: 2019/8/23

from django.conf.urls import url

from .views import OrderView, OrderInView, OrderOutView

order_url_patterns = [
    url(r'order/', OrderView.as_view(), name="order-main"),
    url(r'order/in', OrderInView.as_view(), name="order-in"),
    url(r'order/out', OrderOutView.as_view(), name="order-out"),
]