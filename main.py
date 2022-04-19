# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import pytest
from loggers import JFMlogging

logger = JFMlogging().getloger()


def init_env():
    cmd = "python -m uiautomator2 clear-cache"
    subprocess.call(cmd, shell=True)
    cmd = "python -m uiautomator2 init"
    subprocess.call(cmd, shell=True)
    logger.info("初始化运行环境!")


def init_report():
    cmd = "allure generate ./reports/result -o ./reports/html/ --clean"
    subprocess.call(cmd, shell=True)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/reports/html/" + "index.html"
    logger.info("报告地址:{}".format(report_path))
    # cmd = "allure open -h 127.0.0.1 -p 8883 ./reports/html/"
    # subprocess.call(cmd, shell=True)
    # logger.info("打开测试报告")


if __name__ == '__main__':
    init_env()
    pytest.main(['-s', '-v', 'testcase/case/', '-q', '--alluredir', './reports/result'])
    init_report()

