#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: vv
# Date: 2019/8/22

from libs.enum import Enum

class USER_STATUS(Enum):
    OK          = (1, "正常")
    FREEZE      = (2, "冻结")

class BACK_TYPE(Enum):
    GONGSHANG   = (1, "中国工商银行")
    NONGYE      = (2, "中国农业银行")
    ZHONGGUO    = (3, "中国银行")
    JIANSHE     = (4, "中国建设银行")
    JIAOTONG    = (5, "中国交通银行")
    YOUZHENG    = (6, "中国邮政储蓄银行")
    ZHAOSHANG   = (7, "中国招商银行")
    PUFA        = (8, "中国浦发银行")
    ZHONGXIN    = (9, "中信银行")
    GUANGDA     = (10, "中国光大银行")
    HUAXIA      = (11, "中国华夏银行")
    MINSHENG    = (12, "中国民生银行")
    GUANGFA     = (13, "中国广发银行")
    OTHERS      = (50, "其他")


