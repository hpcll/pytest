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

from config import *
from loggers import JFMlogging
from appium import webdriver
import subprocess

logger = JFMlogging().getloger()


def init_driver():
    '''
    初始化driver
    is_clear:清除数据
    :return:
    '''
    try:
        caps = {}
        caps["platformName"] = PlatformName
        caps["appium:platformVersion"] = ProductVersion
        caps["appium:deviceName"] = DeviceName
        caps["appium:bundleId"] = iOS_bundle_id
        caps["appium:udid"] = Udid
        # caps["appium:includeSafariInWebviews"] = True
        # caps["appium:newCommandTimeout"] = newCommandTimeout
        # caps["appium:connectHardwareKeyboard"] = True
        caps["appium:usePrebuiltWDA"] = False
        caps["appium:useXctestrunFile"] = False
        caps["appium:skipLogCapture"] = True
        # caps["appium:webDriverAgentUrl"] = "http://127.0.0.1:8100"
        d = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        logger.info("当前连接的设备:{} 设备UDID为: {}".format(DeviceName, Udid))
        return d

    except Exception as e:
        logger.info("初始化driver异常!{}".format(e))

