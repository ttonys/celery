# -*- coding: utf-8 -*-
# @Time    : 2022/4/12 4:33 下午
# @FileName: main.py
# @Software: PyCharm
from tasks import demo01, demo02


if __name__ == "__main__":
    res01 = demo01.delay(1, 2)
    res02 = demo02.delay(4, 4)