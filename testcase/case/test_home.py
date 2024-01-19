import pytest
import allure
from testcase.module.HomePage import HOME
from loggers import JFMlogging

logger = JFMlogging().getloger()


# allure.feature定义报告
@allure.feature("首页测试")
@pytest.mark.usefixtures('function_fixture2')
class TestHome:
    @allure.title("首页模块")
    @pytest.fixture()
    def init(self):
        print("\n==============================init=============================")
        print(self.driver)
        self.home = HOME(self.driver)
        logger.info("初始化首页模块")
        yield self.home
        logger.info("结束首页模块")

    def test_home_setting(self, init):
        init.wait_sleep(5)
        "打开设备并返回发现页"
        print("\n==============================test_home_setting=============================")
        init.in_mine()  # 进入我的页面
        init.in_find()  # 进入发现页面
        init.click_sub()  # 进入订阅面

    # def test_home_sub(self, init):
    #     "打开首页订阅页面"
    #     print("\n==============================test_home_setting=============================")
    #     init.click_sub()
