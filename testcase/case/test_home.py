import pytest

from testcase.module.home import Home
from loggers import JFMlogging
logger = JFMlogging().getloger()
from config import *

@pytest.mark.usefixtures('function_fixture')
class TestHome:

    @pytest.fixture()
    def init(self,scope="class"):
        self.home = Home(self.driver)
        logger.info("初始化首页模块")
        yield self.home
        logger.info("结束首页模块")

    def test_home_setting(self,init):
        init.setting_tab()
