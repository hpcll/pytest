# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import os
import subprocess
from loggers import JFMlogging

logger = JFMlogging().getloger()


def init_env():
    cmd = "python -m uiautomator2 clear-cache"
    subprocess.call(cmd, shell=True)
    cmd = "python -m uiautomator2 init"
    subprocess.call(cmd, shell=True)
    logger.info("初始化运行环境!")


def init_report():
    # cmd = "allure generate --clean data -o reports"
    # subprocess.call(cmd, shell=True)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "\\report\\" + "index.html"
    # print("报告地址:{}".format(report_path))
    logger.info("报告地址:{}".format(report_path))


if __name__ == '__main__':
    init_env()
    pytest.main(["-s"])
    # init_report()
    # pytest.main(["-s", "test_home.py"])
