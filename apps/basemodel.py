#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: vv
# Date: 2019/8/22


from django.db import models


class BaseModel(models.Model):

    class Meta:
        abstract = True

    is_online = models.BooleanField(verbose_name=u"是否有效", default=True)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True, db_index=True)
    is_deleted = models.BooleanField(verbose_name='是否删除', default=False)
