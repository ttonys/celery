# -*- coding: utf-8 -*-
# @Time    : 2022/4/12 4:33 下午
# @FileName: run.py
# @Software: PyCharm
from .tasks import app
from .tasks import demo01, demo02, demo03
from utils.logger import Logger

lg = Logger()


def run_demo01():
    """
    执行基本的celery任务
    :return:
    """
    demo01.delay(1, 2)


def run_demo02():
    """
    celery任务传参到任务函数
    :return:
    """
    demo02.delay(4, 4)


def run_demo03():
    """
    apply_async可传入复杂参数进行额外配置，如time_limit限定时限为5s，使任务执行失败
    :return:
    """
    demo03.apply_async((10, 20), time_limit=11)


# def run_demo04():
#     app.send_task('run.add', args=[3, 4])


def main():
    run_demo01()
    run_demo02()
    run_demo03()
    # run_demo04()
