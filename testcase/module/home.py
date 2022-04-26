from time import sleep
from testcase.module.Base import Base
from loggers import JFMlogging
import allure
logger = JFMlogging().getloger()

sub_id = "FREE TRIAL"
create_id = "filto other 300 07"
mypage_id = "我的"
discover_id = "发现"


class Home(Base):

    # 测试用例
    def __init__(self, driver):
        super().__init__(driver)
        print(self.get_windowsize())
        print(driver)
        # self.base = Base(driver)

    @allure.story("进入我的页面")
    def setting_tab(self):
        print(self.d)
        self.click(mypage_id, mypage_id)#打开设置页
        sleep(1)
        self.Screenshot_img(mypage_id)
        logger.info("从首页进入我的")

    @allure.story("返回发现页")
    def discover_tab(self):
        logger.info("返回发现页1")
        self.click(discover_id, discover_id)
        sleep(1)
        self.Screenshot_img(discover_id)
        logger.info("返回发现页")
