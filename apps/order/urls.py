#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: vv
# Date: 2019/8/23

from django.conf.urls import url

from .views import OrderView, OrderInView, \
    OrderOutView, OrderPreMatchView, OrderPostMatchView, OrderSplitView

order_url_patterns = [
    url(r'order/$', OrderView.as_view(), name="order-main"),
    url(r'order/in/$', OrderInView.as_view(), name="order-in"),
    url(r'order/out/$', OrderOutView.as_view(), name="order-out"),
    url(r'order/pre_match/$', OrderPreMatchView.as_view(), name="order-pre-match"),
    url(r'order/post_match/$', OrderPostMatchView.as_view(), name="order-post-match"),
    url(r'order/split/$', OrderSplitView.as_view(), name="order-split"),
]
