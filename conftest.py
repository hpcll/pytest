# !/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import time

from config import *
import pytest
from driver import init_driver
from loggers import JFMlogging
logger = JFMlogging().getloger()


def function_fixture():
    def driver_teardown():
        os.popen("tidevice fsync -B {} rm /Documents/log.json".format(iOS_bundle_id))
        print("清除 log")


@pytest.fixture()
def function_fixture2(request):
    request.instance.driver = init_driver()
    logger.info("打开APP")
    def driver_teardown():
        logger.info("测试完成，关闭app")
        request.instance.driver.close_app()
    request.addfinalizer(driver_teardown)


@pytest.fixture(scope="class")
def class_fixture():
    d = init_driver()
    logger.info("打开APP")
    yield d
    d.close_app()
    logger.info("测试完成，关闭app")


@pytest.fixture(scope="module")
def module_fixture():
    d = init_driver()
    logger.info("打开APP")
    yield d
    d.close_app()
    logger.info("测试完成，关闭app")


#
# def screen_shot(driver):
#     '''
#     截图操作
#     pic_name:截图名称
#     :return:
#     '''
#     try:
#         fail_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
#         fail_pic = str(fail_time) + "截图"
#         pic_name = os.path.join(screenshot_folder, fail_pic)
#         driver.screenshot("{}.jpg".format(pic_name))
#         logger.info('截图:{}'.format(pic_name))
#         f = open(pic_name, 'rb')  # 二进制方式打开图文件
#         base64_str = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
#         f.close()
#         return base64_str
#     except Exception as e:
#         logger.info("{}截图失败!{}".format(pic_name, e))
