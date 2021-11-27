import pytest

from testcase.module.home import Home
from loggers import JFMlogging

logger = JFMlogging().getloger()


@pytest.mark.usefixtures('function_fixture2')
class TestHome:

    @pytest.fixture()
    def init(self):
        print("==============================init=============================")
        self.home = Home(self.driver)
        logger.info("初始化首页模块")
        yield self.home
        # do something
        logger.info("结束首页模块")

    def test_home_setting(self, init):
        print("==============================test_home_setting=============================")
        init.setting_tab()
