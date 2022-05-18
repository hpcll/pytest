from time import sleep
from testcase.module.Base import Base
from loggers import JFMlogging
import allure
logger = JFMlogging().getloger()

#设置页元素



class SET(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # @allure.story("点击发现页订阅入口")
    # def click_banner(self):
        # self.click(subscribe, subscribe_text)
        # sleep(1)
        # self.Screenshot_img(subscribe_text)
        # logger.info("点击发现页banner完成")