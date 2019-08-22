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
    user_id = models.CharField(null=False, verbose_name="产生动作的用户")
    object_type = models.CharField(db_index=True, null=True, blank=True, max_length=250, verbose_name="动作操作的对象类型")
    object_id_json = models.TextField(null=False, blank=False, verbose_name="动作操作的对象的id (json serialized)")
    message = models.TextField(null=True, blank=True, verbose_name="动作详情描述")
    package_new = models.IntegerField(verbose_name=u'动作所在的模块', choices=OPERATE_LOG_PACKAGE)
    action_new = models.IntegerField(verbose_name=u'动作名称', choices=OPERATE_LOG_ACTION)

