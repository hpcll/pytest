import os
import re
import time

from config import *
import pytest
from deiver import Driver


@pytest.fixture(scope="function")
def my_fixture():
    d = Driver().init_driver()
    d.app_start(Android_bundle_id, lanuch_activity, stop=True)
    print("打开app")
    print(type(d))
    yield d
    os.popen("adb shell am force-stop com.video.editor.filto")
    print("测试完成，关闭app")

"""
@pytest.fixture(scope="function")
def my_fixture(request):
    print("自动化测试开始!")
    request.instance.driver = Driver().init_driver()
    print("driver初始化")
    request.instance.driver.app_start(Android_bundle_id, lanuch_activity, stop=True)
    time.sleep(lanuch_time)
    def driver_teardown():
        print("自动化试结束!")
        request.instance.driver.app_stop(Android_bundle_id)
    request.addfinalizer(driver_teardown)
"""


# """
#         msg = os.popen("adb devices").read()
#         deviceId = re.findall(r'([\w]+)\tdevice', msg)[0]
#         cls.d = u2.connect(deviceId)
# """
