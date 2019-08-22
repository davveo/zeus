#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: vv
# Date: 2019/8/22


from django.apps import AppConfig


class LogConfig(AppConfig):
    name = 'apps.logs'
    verbose_name = '日志管理'


    def ready(self):
        pass