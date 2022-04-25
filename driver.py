import os
import re
import uiautomator2 as u2

# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : hupc
@Time    : 2021/11/10 18:34
@describe: 创建Appium
"""
import time
import uiautomator2
from config import *
from loggers import JFMlogging
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

logger = JFMlogging().getloger()


def init_driver():
    '''
    初始化driver
    is_clear:清除数据
    :return:
    '''
    try:
        caps = {}
        caps["platformName"] = "iOS"
        caps["appium:platformVersion"] = "14.6"
        caps["appium:deviceName"] = "iPhone8 PLUS"
        caps["appium:bundleId"] = "com.pinsotech.filto"
        caps["appium:udid"] = "f1273ada5252d874bb994cf9bb4882c61c6f5109"
        caps["appium:includeSafariInWebviews"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True
        d = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # d = uiautomator2.connect(deviceid)
        # logger.info("当前连接的设备: {}_{}   设备ID为: {}".format(d.device_info["brand"], device_name, deviceid))
        # time.sleep(5)
        # logger.info(device_name)
        # logger.info("设备信息:{}".format(d.info))
        # # 设置全局寻找元素超时时间
        # d.wait_timeout = wait_timeout  # default 20.0
        # # 设置点击元素延迟时间
        # d.click_post_delay = click_post_delay
        return d

    except Exception as e:
        logger.info("初始化driver异常!{}".format(e))


class Driver():
    pass
