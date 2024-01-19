# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os, re

#部分设备信息获取
Udid = os.popen("idevice_id -l").read().replace('\n', '').replace('\r', '')
DeviceName = os.popen("ideviceinfo -u {} -k DeviceName".format(Udid)).read().replace('\n', '').replace('\r', '')
ProductVersion = os.popen("ideviceinfo -u {} -k ProductVersion".format(Udid)).read().replace('\n', '').replace('\r', '')
PlatformName = "iOS"
#ios app包名
iOS_bundle_id = "com.pinsotech.filto"
# iOS_bundle_id = "com.gpower.filtoDevelopment"
#ideviceinfo -u 00008120-001C3C463E63C01E -k DeviceName
#ideviceinfo -u 00008120-001C3C463E63C01E -k ProductVersio

#Android APP包名
Android_bundle_id = "com.video.editor.filto"

#Filto首页activity
lanuch_activity = "com.gameinlife.color.paint.filto.activity.ActivityChooser"

# 设置全局寻找元素超时时间
wait_timeout = 20

# 设置点击元素延迟时间
click_post_delay = 20

# #iOS UDID
# # iOS_UDID="f1273ada5252d874bb994cf9bb4882c61c6f5109"   #iPhone 8Plus
# iOS_UDID = "00008020-00114CC63402002E"  #iPhone XsMax
#客户端接收命令超时时间
newCommandTimeout = 120

lanuch_time = 5

#获取当前时间
now_time = datetime.datetime.now()
#将当前时间按自己想要的格式转换
time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d_%H-%M-%S')
#截图储存路径
path = '{}/screenshots/{}_{}'.format(os.getcwd(), time_str, DeviceName)
