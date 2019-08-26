#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: vv
# Date: 2019/8/26

from django.http.response import JsonResponse

def login(request):

    return JsonResponse({"error": 0, "msg": '成功', "data": {}})


def logout(request):

    return JsonResponse({"error": 0, "msg": '成功', "data": {}})