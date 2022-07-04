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

album_index = "album_source_1"
album_index_text = "相册页选择资源"


class Album(Base):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.story("退出相册页")
    def click_album_back(self):
        self.default_click_screenshot(album_back, album_back_text)

    @allure.story("切换至视频tab")
    def click_album_video(self):
        self.default_click_screenshot(album_video, album_video_text)

    @allure.story("切换至图片tab")
    def click_album_video(self):
        self.default_click_screenshot(album_image, album_image_text)

    @allure.story("点击相册页素材")
    def click_album_video(self):
        self.default_click_screenshot(album_index, album_index_text)



