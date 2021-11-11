import os,re
import uiautomator2 as u2

msg = os.popen("adb devices -l").read()
msg1 = os.popen("adb devices").read()
deviceId_list = re.findall(r'([\w]+)\tdevice', msg1)
deviceId_name_list = re.findall(r"device.*model:(.*)\sdevice", msg)
iOS_bundle_id = "com.pinsotech.filto"
Android_bundle_id = "com.video.editor.filto"
lanuch_activity = "com.gameinlife.color.paint.filto.activity.ActivityChooser"
wait_timeout = 20
click_post_delay = 20
iOS_deviceId="86616cbaa40e52d3f9236ec982dd6f1e933a44bd"
lanuch_time = 5