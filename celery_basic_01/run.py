# -*- coding: utf-8 -*-
# @Time    : 2022/4/12 4:33 下午
# @FileName: run.py
# @Software: PyCharm
import sys
from .tasks import app
from .tasks import demo01, demo02, demo03, demo05, demo06
from utils.logger import Logger

lg = Logger()


def run_demo01():
    """
    执行基本的celery任务
    :return:
    """
    lg.logger.info(f"执行{sys._getframe().f_code.co_name}方法")
    demo01.delay(1, 2)


def run_demo02():
    """
    celery通过bind传参到任务函数
    :return:
    """
    lg.logger.info(f"执行{sys._getframe().f_code.co_name}方法")
    demo02.delay(4, 4)


def run_demo03():
    """
    apply_async可传入复杂参数进行额外配置，如time_limit限定时限为5s，使任务执行失败
    :return:
    """
    lg.logger.info(f"执行{sys._getframe().f_code.co_name}方法")
    demo03.apply_async((10, 20), time_limit=11)


def run_demo04():
    """
    send_task可以发送未被注册的异步任务，即没有被celery.task装饰的任务
    todo: 存在bug,key-error
    :return:
    """
    lg.logger.info(f"执行{sys._getframe().f_code.co_name}方法")
    app.send_task('tasks.py.demo04', (3, 4))


def run_demo05():
    """
    celery自动路由
    通过queue参数配置可为分配任务到指定路由队列
    运行celery指定-Q参数可对指定路由进行消费,如： celery -A celery_basic_01.tasks worker -l info -Q demo05
    :return:
    """
    lg.logger.info(f"执行{sys._getframe().f_code.co_name}方法")
    demo05.apply_async((2, 2), queue='demo05')


def run_demo06():
    """
    通过config配置，手动创建demo06路由队列，将此任务发送到demo06队列
    :return:
    """
    lg.logger.info(f"执行{sys._getframe().f_code.co_name}方法")
    demo06.apply_async((2, 2))


def main():
    run_demo01()
    run_demo02()
    run_demo03()
    # run_demo04()
    run_demo05()
    run_demo06()
