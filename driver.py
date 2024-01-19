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
from appium.options.common.base import AppiumOptions

logger = JFMlogging().getloger()


def init_driver():
    """
    初始化driver
    is_clear:清除数据
    :return:
    """

    try:

        options = AppiumOptions()
        options.load_capabilities({
            "platformName": PlatformName,
            "appium:platformVersion": ProductVersion,
            "appium:deviceName": DeviceName,
            "appium:bundleId": iOS_bundle_id,
            "appium:udid": Udid,
            "appium:automationName": "XCUITest",
            "appium:includeSafariInWebviews": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True
        })

        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        return driver

    except Exception as e:
        logger.info("初始化driver异常!{}".format(e))


if __name__ == '__main__':
    d = init_driver()
    window_size = d.get_window_size()
    width = int(window_size["width"])
    height = int(window_size["height"])
    print(width, height)
