import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# capabilities = dict(
#     platformName='iOS',
#     automationName='xcuitest',
#     deviceName='iPhone14Pro',
#     appPackage='com.pinsotech.filto',
#     appActivity='com.gameinlife.color.paint.filto.activity.ActivityChooser',
#     language='cn',
#     locale='china'
# )

capabilities = {
    "platformName": "iOS",
    "appium:platformVersion": "17.2.1",
    "appium:deviceName": "叔叔胡的iPhone",
    "appium:bundleId": "com.pinsotech.filto",
    "appium:udid": "00008120-001C3C463E63C01E",
    "appium:automationName": "XCUITest",
    "appium:includeSafariInWebviews": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
}

appium_server_url = 'http://localhost:4723'
driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
window_size = driver.get_window_size()
width = int(window_size["width"])
height = int(window_size["height"])
print(width, height)

# class TestAppium(unittest.TestCase):
#     def setUp(self) -> None:
#         self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
#
#     def tearDown(self) -> None:
#         if self.driver:
#             self.driver.quit()
#
#     def test_find_battery(self) -> None:
#         el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
#         el.click()
#
# if __name__ == '__main__':
#     unittest.main()
