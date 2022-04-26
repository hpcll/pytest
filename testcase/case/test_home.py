import pytest
import allure
from testcase.module.Home import Home
from loggers import JFMlogging
logger = JFMlogging().getloger()


#allure.feature定义报告
@allure.feature("首页测试")
@pytest.mark.usefixtures('function_fixture2')
class TestHome:
    @allure.title("首页模块")
    @pytest.fixture()
    def init(self):
        print("==============================init=============================")
        print(self.driver)
        self.home = Home(self.driver)
        logger.info("初始化首页模块")
        yield self.home
        # do something
        logger.info("结束首页模块")

    def test_home_setting(self, init):
        init.wait_sleep(5)
        "打开设备并返回发现页"
        print("==============================test_home_setting=============================")
        init.setting_tab()
        init.wait_sleep(3)
        init.discover_tab()
