#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: vv
# Date: 2019/8/22

import json
import logging
from celery import shared_task
from .models import OperationLog
from utils.gen_id import IDGenerator

exception_logger = logging.getLogger('exception_logger')
operation_logger = logging.getLogger('operation_logger')

@shared_task
def operation_log_record(data):
    """
    异步记录操作日志
    :param data:
    :return:
    """
    # 操作入库
    generator = IDGenerator()
    while True:
        try:
            request_id = generator.generate_id(id_length=12)
            OperationLog.objects.create(
                request_id=request_id,
                user_id=data['user_id'],
                message=data['message'],
                module=data['module'],
                action=data['action']
            )
            break
        except Exception as e:
            pass

    # 记录日志
    data.update({'request_id': request_id})
    operation_logger.info(json.dumps(json.dumps(data), ensure_ascii=True))





@shared_task
def exception_log_record(data):
    """
    异步记录异常信息
    :param data:
    :return:
    """

    exception_logger.info(data)