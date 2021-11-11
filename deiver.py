import os
import re
import uiautomator2 as u2

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : hupc
@Time    : 2021/11/10 18:34
@describe: 创建uiautomator2
"""
import time
import wda
# import subprocess
import uiautomator2
from config import *


# logger = JFMlogging().getloger()

class Driver():


    def init_driver(self):
        print("hhhhhh")
        '''
        初始化driver
        is_clear:清除数据
        :return:
        '''
        try:
            print("jjjj")
            # print(deviceId_list,deviceId_name_list)
            for i in range(0, len(deviceId_list)):
                device_name = deviceId_name_list[i]
                deviceid = deviceId_list[i]
                # 手机的IP
                d = uiautomator2.connect(deviceid)
                print("当前连接的设备: {}_{}   设备ID为: {}".format(d.device_info["brand"], device_name, deviceid))
                d.app_start(Android_bundle_id, lanuch_activity, stop=True)
                print("deiver文件")
                time.sleep(5)
            # logger.info(device_name)
            # d = u2.connect(deviceId)
            # d = ut2.connect("192.168.129.93")
            #logger.info("设备信息:{}".format(d.info))
            # 设置全局寻找元素超时时间
            #     d.wait_timeout = wait_timeout  # default 20.0
                # 设置点击元素延迟时间
                # d.click_post_delay = click_post_delay
                #d.service("uiautomator").stop()
                # 停止uiautomator 可能和atx agent冲突
                # logger.info("连接设备:{}".format(device_name))
                print("连接设备:{}_{}".format(d.device_info["brand"], device_name))
                print(type(d))
                return d

        except Exception as e:
            print("初始化driver异常!{}".format(e))
            # logger.info("初始化driver异常!{}".format(e))



    def init_ios_driver(self, iOS_deviceId,iOS_bundle_id):
        try:
            d = wda.Client('http://localhost:8100')
            # d.start_app(bundle_id)
            c = wda.USBClient(iOS_deviceId, port=8100,wda_bundle_id=iOS_bundle_id)
            time.sleep(5)
            return d
        except Exception as e:
            print("初始化ios端driver异常!{}".format(e))
            # logger.info("初始化ios端driver异常!{}".format(e))



#
# # os.popen("adb shell am force-stop com.video.editor.filto")#关闭APP
#
if __name__ == '__main__':
    d = Driver()
    d.init_driver()

