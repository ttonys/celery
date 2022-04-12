# -*- coding: utf-8 -*-
# @Time    : 2022/4/12 4:33 下午
# @FileName: main.py
# @Software: PyCharm
from tasks import demo01, demo02
from utils.logger import Logger

lg = Logger()

if __name__ == "__main__":
    lg.logger.info("test")
    lg.logger.warning("test")
    res01 = demo01.delay(1, 2)
    res02 = demo02.delay(4, 4)