#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: vv
# Date: 2019/8/23

import time
import struct
import random

class IDGenerator(object):
    def _get_timestamp(self):
        """
        获取当前时间戳
        :return:
        """
        return int(time.time() * 1000)

    def generate(self):
        """
        生成器
        :return:
        """
        now = self._get_timestamp()
        series_id = random.randrange(0, 1 << 22)
        high = now >> 10
        low = (now & 0xffc00000) | series_id
        return struct.pack(">II", high, low)


