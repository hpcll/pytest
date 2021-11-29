from time import sleep
from testcase.module.base import Base
from loggers import JFMlogging

logger = JFMlogging().getloger()

setting_resourceId = "com.video.editor.filto:id/ll_home_bottom_setting"
discover_resourceId = "com.video.editor.filto:id/ll_home_bottom_discover"
setting = "设置"
discover = "发现页"


class Home(Base):
    # 测试用例

    def __init__(self, driver):
        super().__init__(driver)
        self.base = Base(driver)

    def setting_tab(self):
        self.base.click(setting_resourceId, setting)#打开设置页
        sleep(1)
        self.base.Screenshot_img(setting)
        logger.info("从首页进入设置页")
        self.base.click(discover_resourceId, discover)
        sleep(1)
        self.base.Screenshot_img(discover)
        logger.info("返回发现页")
