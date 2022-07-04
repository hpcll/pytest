from time import sleep
from testcase.module.base import Base
from loggers import JFMlogging
import allure

logger = JFMlogging().getloger()


edit_back = "edit_back"
edit_back_text = "编辑页返回按钮"

edit_back_yes = "edit_back_yes"
edit_back_yes_text = "退出编辑页弹窗确认按钮"

edit_back_no = "edit_back_no"
edit_back_no_text = "退出编辑页弹窗取消按钮"

edit_save = "edit_save"
edit_save_text = "编辑页保存按钮"

edit_effect = "edit_effect"
edit_effect_text = "编辑页特效tab"

edit_filter = "edit_filter"
edit_filter_text = "编辑页滤镜tab"

edit_adjust = "edit_adjust"
edit_adjust_text = "编辑页调整tab"

edit_sticker = "edit_sticker"
edit_sticker_text = "编辑页贴纸tab"

edit_font = "edit_font"
edit_font_text = "编辑页文字tab"

edit_canvas = "edit_canvas"
edit_canvas_text = "编辑页画布tab"

edit_music = "edit_music"
edit_music_text = "编辑页音乐tab"

edit_clip = "edit_clip"
edit_clip_text = "编辑页剪辑tab"


class Edit(Base):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.story("点击编辑页返回入口")
    def click_edit_back(self):
        self.default_click_screenshot(edit_back, edit_back_text)

    @allure.story("退出编辑页弹窗确认按钮")
    def click_edit_back_yes(self):
        self.default_click_screenshot(edit_back_yes, edit_back_yes_text)

    @allure.story("退出编辑页弹窗取消按钮")
    def click_edit_back_no(self):
        self.default_click_screenshot(edit_back_no, edit_back_no_text)

    @allure.story("点击编辑页保存入口")
    def click_edit_save(self):
        self.default_click_screenshot(edit_save, edit_save_text)

    @allure.story("点击编辑页特效tab")
    def click_edit_effect(self):
        self.default_click_screenshot(edit_effect, edit_effect_text)

    @allure.story("点击编辑页滤镜tab")
    def click_edit_filter(self):
        self.default_click_screenshot(edit_filter, edit_filter_text)

    @allure.story("点击编辑页调整tab")
    def click_edit_adjust(self):
        self.default_click_screenshot(edit_adjust, edit_adjust_text)

    @allure.story("点击编辑页贴纸tab")
    def click_edit_adjust(self):
        self.default_click_screenshot(edit_sticker, edit_sticker_text)

    @allure.story("点击编辑页文字tab")
    def click_edit_adjust(self):
        self.default_click_screenshot(edit_sticker, edit_sticker_text)

    @allure.story("点击编辑页画布tab")
    def click_edit_adjust(self):
        self.default_click_screenshot(edit_canvas, edit_canvas_text)

    @allure.story("点击编辑页音乐tab")
    def click_edit_adjust(self):
        self.default_click_screenshot(edit_music, edit_music_text)

    @allure.story("点击编辑页剪辑tab")
    def click_edit_adjust(self):
        self.default_click_screenshot(edit_clip, edit_clip_text)

