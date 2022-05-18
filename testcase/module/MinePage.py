from time import sleep
from testcase.module.Base import Base
from loggers import JFMlogging
import allure
logger = JFMlogging().getloger()

# 我的页面元素
record = "source:record"
record_text = "历史记录"

setting = "page:setting"
setting_text = "设置页"


class Mine(Base):
    def __init__(self, driver):
        super().__init__(driver)
        # print(self.get_windowsize())
        # print(driver)
        # # self.base = Base(driver)

    @allure.story("点击历史记录")
    def click_plus(self):
        # print(self.d)
        self.click(record, record_text)  # 点击 +
        sleep(1)
        self.Screenshot_img(record_text)
        # logger.info("点击首页+")

    @allure.story("点击设置页按钮")
    def click_plus(self):
        # print(self.d)
        self.click(setting, setting_text)  # 点击 +
        sleep(1)
        self.Screenshot_img(setting_text)
        # logger.info("点击首页+")