#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: vv
# Date: 2019/8/23

import random

class IDGenerator(object):

    def generate_id(sefl, id_length):
        return str(random.randint(10 ** (id_length - 1), 10 ** id_length - 1))


