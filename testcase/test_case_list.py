from time import sleep
from deiver import Driver
import pytest


class Test_case_list:
    # 测试用例

    def test02_open_setting(self,my_fixture):
        """从首页进入设置页"""
        my_fixture(resourceId="com.video.editor.filto:id/ll_home_bottom_setting").click()  # 打开设置
        sleep(1)
        # # # Screenshot_img(device_name, "设置")
        my_fixture(resourceId="com.video.editor.filto:id/ll_home_bottom_discover").click()  # 返回发现页
        print("回到发现页")



