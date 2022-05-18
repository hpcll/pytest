import subprocess

import allure
import pytest

from config import *
from appium.webdriver.common.appiumby import AppiumBy
import json
from driver import init_driver
from loggers import JFMlogging

logger = JFMlogging().getloger()

d = init_driver()


def click(element):
    '''
    元素点击
    driver: 操作对象
    element:元素名称
    logtext:打印log的文案
    xpath使用方法
    1.包含
    d.xpath(u"//android.widget.TextView[contains(@text,'购买 ¥')]").click()
    2.全匹配
    d.xpath(u"//android.widget.TextView[@text='购买 ¥4.99']").click()
    3.匹配开始字符
    d.xpath(u"//android.widget.TextView[starts-with(@text,'购买 ¥')]").click()
    :return:
    '''
    if str(element).startswith("filto"):
        d.find_element(AppiumBy.ACCESSIBILITY_ID, element).click()
    elif re.findall("//", str(element)):
        d.find_element(AppiumBy.XPATH, element).click()
    elif re.findall("\*\*", str(element)):
        d.find_element(AppiumBy.IOS_CLASS_CHAIN, element).click()
    elif str(element).startswith("label"):
        d.find_element(AppiumBy.IOS_PREDICATE, element).click()
    else:
        d.find_element(AppiumBy.ACCESSIBILITY_ID, element).click()
    # logger.info("点击元素:{}".format(logtext))



@pytest.fixture(scope="session")
def teardown_function():
    os.popen("tidevice fsync -B {} rm /Documents/log.json".format(iOS_bundle_id))
    print("\n清除 log")


case1 = [
    "source:banner",
    "media_type:video",
    "function:adjust",
    "in_function:none",
    "content:C2",
    "edit_page",
    "function_use",#功能使用
    "content_use",#内容使用
    # "edit_save"
]

for i in case1:
    click(i)
a = os.popen("tidevice fsync -B {} cat /Documents/log.json".format(iOS_bundle_id)).read()  # 获取手机的日志
a = json.loads(a)
print(type(a))



@allure.feature("编辑页访问")
class Testpage:
    @allure.title("编辑页访问")
    def test_EditpPageAccess(self):
        expect = {"name": "pvbegin_edit", "params": [
            {"media_type": "media_type:video", "launch_type": "user", "is_sub": False, "source": "source:banner",
             "session_cnt": 2, "session_day": 1}]}
        with allure.step("编辑页访问埋点校验"):
            assert a[0] == expect
            logger.info("校验成功")


    @allure.title("功能使用")
    def test_EditpPageAccess1(self):
        expect = a[1]
        with allure.step("功能使用埋点校验"):
            assert a[1] == expect
            logger.info("校验成功")



    @allure.title("内容使用")
    def test_EditpPageAccess2(self):
        expect = a[2]
        with allure.step("内容埋点校验"):
            assert a[2] == expect
            logger.info("校验成功")

