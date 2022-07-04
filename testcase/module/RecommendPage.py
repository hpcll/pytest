from time import sleep
from testcase.module.base import Base
from loggers import JFMlogging
import allure
logger = JFMlogging().getloger()

# 发现页元素
subscribe = "banner_subscribe"
subscribe_text = "发现页订阅入口"

banner = "source_banner"
banner_text = "发现页banner"

recommend = "source_recommend"
recommend_text = "发现页信息流素材"


class Find(Base):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.story("点击发现页订阅入口")
    def in_subscribe(self):
        self.click(subscribe, subscribe_text)
        sleep(1)
        self.Screenshot_img(subscribe_text)
        # logger.info("点击发现页banner完成")

    @allure.story("点击发现页banner")
    def click_banner(self):
        self.click(banner, banner_text)
        sleep(1)
        self.Screenshot_img(banner_text)
        # logger.info("点击发现页banner完成")

    @allure.story("点击发现页信息流素材")
    def click_recommend(self):
        self.click(recommend, recommend_text)
        sleep(1)
        self.Screenshot_img(recommend_text)
        # logger.info("点击发现页信息流素材")

