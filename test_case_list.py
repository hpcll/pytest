import pytest
import uiautomator2 as u2
class Test_case_list():

    def test_01_open_app(self):
        print("open app")

    def test_02_open_home(self):
        print("打开 home")

    def test_03_in_photo(self):
        print("进入 相册页")


if __name__ == '__main__':
    pytest.main(["-s"])
    # pytest.main(["-s", "test_case_list.py"])

