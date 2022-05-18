import os, re
import time
from config import *
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from driver import init_driver
from loggers import JFMlogging

logger = JFMlogging().getloger()

d = init_driver()


def click(element):
    '''
    元素点击
    driver: 操作对象
    element:元素名称
    logtext:打印log的文案
    xpath使用方法
    1.包含
    d.xpath(u"//android.widget.TextView[contains(@text,'购买 ¥')]").click()
    2.全匹配
    d.xpath(u"//android.widget.TextView[@text='购买 ¥4.99']").click()
    3.匹配开始字符
    d.xpath(u"//android.widget.TextView[starts-with(@text,'购买 ¥')]").click()
    :return:
    '''
    if str(element).startswith("filto"):
        d.find_element(AppiumBy.ACCESSIBILITY_ID, element).click()
    elif re.findall("//", str(element)):
        d.find_element(AppiumBy.XPATH, element).click()
    elif re.findall("\*\*", str(element)):
        d.find_element(AppiumBy.IOS_CLASS_CHAIN, element).click()
    elif str(element).startswith("label"):
        d.find_element(AppiumBy.IOS_PREDICATE, element).click()
    else:
        d.find_element(AppiumBy.ACCESSIBILITY_ID, element).click()
    # logger.info("点击元素:{}".format(logtext))


def find_elements(element, timeout=1):
    '''
    查找元素是否存在当前页面
    :return:
    '''
    is_exited = False
    try:
        while timeout > 0:
            xml = d.page_source
            if re.findall(element, xml):
                is_exited = True
                logger.info("查询到{}".format(element))
                break
            else:
                timeout -= 1
    except Exception as e:
        logger.info("{}查找失败!{}".format(element, e))
    finally:
        return is_exited


def assert_exited(element):
    '''
    断言当前页面存在要查找的元素,存在则判断成功
    :param driver:
    :return:
    '''
    assert find_elements(element) == True, "断言{}元素存在,失败!".format(element)
    logger.info("断言{}元素存在,成功!".format(element))


def geteleByPredicate(con):
    '''
    通过ByPredicate方式获得元素
    :param con: condition
    :return: 元素
    '''
    ele = d.find_element_by_ios_predicate(con)
    return ele


def toLeftSwipeByPredicate(con):
    ele = geteleByPredicate(con)
    d.execute_script("mobile:swipe", {"direction": "left", 'element': ele, "duration": 1})


def is_Editor_Page():
    fined = False;
    while fined == False:
        fined = find_elements("filto321 2")
        print("目前未在编辑页")
    time.sleep(10)
    # return fined


def move_to(key1, key2):
    """从某个元素滑动至某个元素"""
    ele1 = d.find_element(AppiumBy.ACCESSIBILITY_ID, key2)
    # 视频按钮元素
    ele2 = d.find_element(AppiumBy.ACCESSIBILITY_ID, key1)
    action = TouchAction(d)
    action.long_press(ele2).move_to(ele1).release().perform()


def Screenshot_img(self, mz):
    """截图"""
    if os.path.exists(path):
        logger.info("{}截图中。。。".format(mz))
        self.d.save_screenshot('{}/{}.png'.format(path, mz))
        logger.info("{}截图完成.....".format(mz))
    else:
        os.makedirs(path)
        logger.info("{}截图中。。。".format(mz))
        self.d.save_screenshot('{}/{}.png'.format(path, mz))
        logger.info("{}截图完成.....".format(mz))


def swipe_CategoryTab():
    """滑动编辑页分类tab"""
    # 获得机器屏幕大小x,y
    x = d.get_window_size()['width']
    y = d.get_window_size()['height']
    print(x, y)
    time.sleep(3)
    # # 屏幕向左滑动
    x1 = int(x * 0.35)  # 开始x坐标，相当于屏幕总x值75%处的值，需要计算输出看看
    y1 = int(y * 0.95)  # 开始y坐标，相当于屏幕总y值5%处的值
    x2 = int(x * 0.05)  # 结束x坐标，相当于屏幕总x值25%处的值
    y2 = int(y * 0.95)  # 结束y坐标，相当于屏幕总x值50%处的值
    d.swipe(x1, y1, x2, y2, 1000)


def traverse_tab(list):
    """判断当前 进入的是那个编辑页"""
    for tab in list:
        logger.info("当前进入的是 {}编辑页".format(list))
        while True:
            time.sleep(5)
            if find_elements(tab):
                click(tab)
                logger.info("点击{}".format(tab))
                break
            else:
                time.sleep(3)
                continue
        time.sleep(5 *60) #在当前页面的等待时间


if __name__ == '__main__':
    key1 = "贴纸"
    key2 = "特效"
    key3 = "音乐"
    progress = "filto public 300 05"
    photo_list = ["滤镜", "特效", "调整", "贴纸", "文字", "画布", "音乐"]
    video_list = ["特效", "滤镜", "贴纸", "文字", "画布", "音乐", "剪辑", "调整"]
    time.sleep(3)
    while True:
        if find_elements("发现"):
            continue
        elif find_elements("filto321 1"):
            if find_elements(progress):
                traverse_tab(video_list)
            else:
                traverse_tab(photo_list)
                break
