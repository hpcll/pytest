# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os, re
import uiautomator2 as u2

msg = os.popen("adb devices -l").read()
msg1 = os.popen("adb devices").read()


#获取设备ID和设备名称
deviceId_list = re.findall(r'([\w]+)\tdevice', msg1)
deviceId_name_list = re.findall(r"device.*model:(.*)\sdevice", msg)
device_name = deviceId_name_list[0]
deviceid = deviceId_list[0]
# d = u2.connect(deviceid)

# for i in range(0, len(deviceId_list)):
#    device_name = deviceId_name_list[i]
#    deviceid = deviceId_list[i]

#ios app包名
iOS_bundle_id = "com.pinsotech.filto"
#Android APP包名
Android_bundle_id = "com.video.editor.filto"
#Filto首页activity
lanuch_activity = "com.gameinlife.color.paint.filto.activity.ActivityChooser"
# 设置全局寻找元素超时时间
wait_timeout = 20
# 设置点击元素延迟时间
click_post_delay = 20
iOS_deviceId="86616cbaa40e52d3f9236ec982dd6f1e933a44bd"
lanuch_time = 5


#获取当前时间
now_time = datetime.datetime.now()
#将当前时间按自己想要的格式转换
time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d_%H-%M-%S')
#截图储存路径
path = '{}/screenshots/{}_{}'.format(os.getcwd(), time_str, device_name)
