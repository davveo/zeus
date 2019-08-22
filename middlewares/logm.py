#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: vv
# Date: 2019/8/22

import time
import json
import datetime
from django.utils.deprecation import MiddlewareMixin
from apps.logs.tasks import operation_log_record, exception_log_record
from libs.exception_info import get_exception_info, get_func_args


    # 操作记录拦截
class LoggingMiddleware(MiddlewareMixin):

        def process_request(self, request):
            request.start_time = time.time()

        def process_response(self, request, response):
            """
            记录后台操作
            :param request:
            :param response:
            :return:
            """
            execute_time = time.time() - request.start_time
            path = request.get_full_path()
            current_user = request.user

            try:
                items = {}
                if request.method == 'GET':
                    items = request.GET.dict()

                elif request.method == 'POST':
                    items = request.POST.dict()

                items = json.dumps(items, ensure_ascii=True, encoding='utf-8')
            except:
                items = ''

            record_data = {
                "user_id": current_user.id,
                "timestamp": datetime.datetime.fromtimestamp(
                            request.start_time
                        ).strftime('%Y-%m-%dT%H:%M:%S+08:00'),
                "request_method": request.method,
                'path': path,
                'execute_time': execute_time,
                "actions": items

            }
            operation_log_record.delay(record_data)
            return response

        def process_exception(self, request, exception):
            """
            出错发送邮件或者短信??
            :param request:
            :param exception:
            :return:
            """
            exc = get_exception_info()
            func_args = get_func_args()

            exception_data = json.dumps(
                    {
                        'stacktrace': exc,
                        'func_args': func_args,
                        'timestamp': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+08:00'),
                    }
                    , ensure_ascii=True, encoding='utf-8'
                )

            exception_log_record.delay(exception_data)
            return




