#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: vv
# Date: 2019/8/22

from libs.enum import Enum

class OPERATE_LOG_PACKAGE(Enum):
    """
    后台操作日志module
    """
    UNIVERSE = (0, u'权限')


class OPERATE_LOG_ACTION(Enum):
    """
    操作日志的action
    """
    CREATE = (1, u'创建')
    MODIFY = (2, u'修改')
    DELETE = (3, u'删除')
    ONLINE = (4, u'上线')
    DOWNONLINE = (5, u'下线')
    SAVE = (6, u'保存')
    RECALL = (7, u'撤回')