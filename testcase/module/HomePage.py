from time import sleep
from testcase.module.Base import Base
from loggers import JFMlogging
import allure
logger = JFMlogging().getloger()


# 首页元素
find = "page:find"
find_text = "发现页"

plus = "source:create"
plus_text = "首页+"

mine = "page:mine"
mine_text = "我的页面"

#
# find_page = {"subscribe": "home_pro", "banner": "source:banner", "plus": "source:create",
#              "recommend": "source:recommend"}
# mine_page = {"setting": "setting", "record": "source:record"}


class HOME(Base):
    def __init__(self, driver):
        super().__init__(driver)
        # print(self.get_windowsize())
        # print(driver)
        # # self.base = Base(driver)

    @allure.story("点击首页+")
    def Click_Plus(self):
        # print(self.d)
        self.click(plus, plus_text)  # 点击 +
        sleep(1)
        self.Screenshot_img(plus_text)
        # logger.info("点击首页+")

    @allure.story("进入发现页面")
    def In_Find(self):
        # print(self.d)
        self.click(find, find_text)
        sleep(1)
        self.Screenshot_img(find_text)
        # logger.info("点击首页+")


    @allure.story("进入发现页面")
    def In_Mine(self):
        # print(self.d)
        self.click(mine, mine_text)
        sleep(1)
        self.Screenshot_img(mine_text)
        # logger.info("点击首页+")
