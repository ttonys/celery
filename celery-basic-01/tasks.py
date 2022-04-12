# -*- coding: utf-8 -*-
# @Time    : 2022/4/12 4:03 下午
# @FileName: tasks.py
# @Software: PyCharm
import time

from celery import Celery
from config import CELERY_BROKER, CELERY_BACKEND

# celery初始化基本配置
app = Celery('celery-basic-01', broker=CELERY_BROKER, backend=CELERY_BACKEND)


@app.task(name='task_demo_01')
def demo01(x, y):
    """
    name显式指定task名称
    :param x:
    :param y:
    :return:
    """
    time.sleep(10)
    return x + y


@app.task(bind=True, name='task_demo_02')
def demo02(self, x, y):
    """
    设定bind=True，可通过self将task实例传入
    :param self:
    :param x:
    :param y:
    :return:
    """
    time.sleep(10)
    return x * y


