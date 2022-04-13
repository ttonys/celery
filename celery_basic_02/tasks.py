# -*- coding: utf-8 -*-
# @Time    : 2022/4/13 4:14 下午
# @FileName: tasks.py
# @Software: PyCharm
import sys

from celery import Celery
from utils.logger import Logger
from config import CELERY_BROKER, CELERY_BACKEND, CELERY_BEAT_SCHEDULE

# celery初始化基本配置
app = Celery('celery_basic_01', broker=CELERY_BROKER, backend=CELERY_BACKEND)
app.conf.update(
    beat_schedule=CELERY_BEAT_SCHEDULE,
)
lg = Logger()


@app.task(bind=True, name="beat_demo01")
def beat_demo01(self, x, y):
    lg.logger.info(f"当前方法名称：{sys._getframe().f_code.co_name} 当前任务id：{self.request.id}")
    return x+y
