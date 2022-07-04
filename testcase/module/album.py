from time import sleep
from testcase.module.base import Base
from loggers import JFMlogging
import allure
logger = JFMlogging().getloger()

album_back = "album_back"
album_back_text = "相册页返回按钮"

album_recent = "album_recent"
album_recent_text = "相册页最近项目按钮"

album_video = "album_video"
album_video_text = "相册页视频按钮"

album_image = "album_image"
album_image_text = "相册页图片按钮"

album_index = "album_1_1"
album_index_text = "相册页选择资源"


class Album(Base):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.story("退出相册页")
    def click_album_back(self):
        # print(self.d)
        self.click(album_back, album_back_text)
        sleep(1)
        self.Screenshot_img(album_back_text)
        logger.info("退出相册页")

    @allure.story("切换至视频tab")
    def click_album_video(self):
        # print(self.d)
        self.click(album_video, album_video_text)
        sleep(1)
        self.Screenshot_img(album_video_text)
        logger.info("切换至视频tab")

    @allure.story("切换至图片tab")
    def click_album_video(self):
        # print(self.d)
        self.click(album_image, album_image_text)
        sleep(1)
        self.Screenshot_img(album_image_text)
        logger.info("切换至图片tab")

    @allure.story("点击相册页素材")
    def click_album_video(self):
        # print(self.d)
        self.click(album_index, album_index_text)
        sleep(1)
        self.Screenshot_img(album_index_text)
        logger.info("点击相册页素材")



