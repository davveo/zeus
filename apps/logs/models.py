#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: vv
# Date: 2019/8/22

from django.db import models
from enums.logs import OPERATE_LOG_ACTION, OPERATE_LOG_PACKAGE

class OperationLog(models.Model):
    class Meta:
        verbose_name="操作记录表"
        db_table="logs_operationlog"
        app_label="logs"

    action_time = models.DateTimeField(null=False, db_index=True, auto_now_add=True, verbose_name="动作发生的时间")
    user_id = models.CharField(null=False, verbose_name="产生动作的用户", max_length=255)
    message = models.TextField(null=True, blank=True, verbose_name="动作详情描述")
    module = models.IntegerField(verbose_name=u'动作所在的模块', choices=OPERATE_LOG_PACKAGE)
    action = models.IntegerField(verbose_name=u'动作名称', choices=OPERATE_LOG_ACTION)
