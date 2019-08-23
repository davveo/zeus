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
    # 记录日志
    operation_logger.info(json.dumps(data, ensure_ascii=True))

    # 操作入库

    OperationLog.objects.get_or_create(

    )

    while True:
        try:
            generator = IDGenerator()
            request_id = generator.generate().encode('hex').upper()
            OperationLog.objects.create(
            )
            break
        except Exception:
            pass





@shared_task
def exception_log_record(data):
    """
    异步记录异常信息
    :param data:
    :return:
    """

    exception_logger.info(data)