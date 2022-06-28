from time import sleep
from testcase.module.base import Base
from loggers import JFMlogging
import allure
logger = JFMlogging().getloger()


# 首页元素
find = "page_find"
find_text = "发现页"

plus = "source_create"
plus_text = "首页+"

mine = "page_mine"
mine_text = "我的页面"

sub_verify = "home_subscription_verify"
sub_verify_text = "首页审核状态下的订阅入口"

sub_not_verify = "home_subscription"
sub_not_verify_text = "首页非审核状态下的订阅入口"

banner = "banner_{}".format("filter-Bling-Sparklers")
banner_text = "filter-Bling-Sparklers"



class HOME(Base):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.story("点击首页+")
    def click_plus(self):
        # print(self.d)
        self.click(plus, plus_text)  # 点击 +
        sleep(1)
        self.Screenshot_img(plus_text)
        # logger.info("点击首页+")

    @allure.story("进入发现页面")
    def in_find(self):
        # print(self.d)
        self.click(find, find_text)
        sleep(1)
        self.Screenshot_img(find_text)
        # logger.info("点击首页+")


    @allure.story("进入发现页面")
    def in_mine(self):
        # print(self.d)
        self.click(mine, mine_text)
        sleep(1)
        self.Screenshot_img(mine_text)
        # logger.info("点击首页+")
