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
banner_text = "banner名为{}的素材".format("filter-Bling-Sparklers")


class HOME(Base):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.story("点击首页+")
    def click_plus(self):
        # print(self.d)
        self.click(plus, plus_text)  # 点击 +
        sleep(1)
        self.screenshot_img(plus_text)
        logger.info("点击首页+")

    @allure.story("进入发现页面")
    def in_find(self):
        # print(self.d)
        self.click(find, find_text)
        sleep(1)
        self.screenshot_img(find_text)
        logger.info("进入发现页面")

    @allure.story("进入我的页面")
    def in_mine(self):
        # print(self.d)
        self.click(mine, mine_text)
        sleep(1)
        self.screenshot_img(mine_text)
        logger.info("进入我的页面")

    @allure.story("点击首页banner")
    def click_banner(self):
        # print(self.d)
        self.click(banner, banner_text)
        sleep(1)
        self.screenshot_img(banner_text)
        logger.info("点击点击首页banner")

    @allure.story("点击首页订阅入口")
    def click_sub(self):
        # print(self.d)
        if self.find_elements(sub_verify):
            self.click(sub_verify, sub_verify_text)
            sleep(1)
            self.screenshot_img(sub_verify_text)
            logger.info("点击首页审核状态下的订阅入口")
        elif self.find_elements(sub_not_verify):
            self.click(sub_verify, sub_not_verify_text)
            sleep(1)
            self.screenshot_img(sub_not_verify_text)
            logger.info("点击非首页审核状态下的订阅入口")
        else:
            print("未找到首页订阅入口。")
