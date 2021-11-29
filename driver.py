import os
import re
import uiautomator2 as u2

# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : hupc
@Time    : 2021/11/10 18:34
@describe: 创建uiautomator2
"""
import time
import uiautomator2
from config import *
from loggers import JFMlogging

logger = JFMlogging().getloger()


def init_driver():
    '''
    初始化driver
    is_clear:清除数据
    :return:
    '''
    try:
        # # print(deviceId_list,deviceId_name_list)
        # for i in range(0, len(deviceId_list)):
        #     device_name = deviceId_name_list[i]
        #     deviceid = deviceId_list[i]
        #     # 手机的IP
        d = uiautomator2.connect(deviceid)
        logger.info("当前连接的设备: {}_{}   设备ID为: {}".format(d.device_info["brand"], device_name, deviceid))
        time.sleep(5)
        logger.info(device_name)
        logger.info("设备信息:{}".format(d.info))
        # 设置全局寻找元素超时时间
        d.wait_timeout = wait_timeout  # default 20.0
        # 设置点击元素延迟时间
        d.click_post_delay = click_post_delay
        return d

    except Exception as e:
        logger.info("初始化driver异常!{}".format(e))


class Driver():
    pass
