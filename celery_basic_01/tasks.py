# -*- coding: utf-8 -*-
# @Time    : 2022/4/12 4:03 下午
# @FileName: tasks.py
# @Software: PyCharm
import sys
import time

from celery import Celery
from utils.logger import Logger
from config import CELERY_BROKER, CELERY_BACKEND, CELERY_TIMEZONE, CELERY_ENABLE_UTC, CELERY_ROUTES, CELERY_QUEUES

# celery初始化基本配置
app = Celery('celery_basic_01', broker=CELERY_BROKER, backend=CELERY_BACKEND)
app.conf.update(
    timezone=CELERY_TIMEZONE,
    enable_utc=CELERY_ENABLE_UTC,
    task_routes=CELERY_ROUTES,
    task_queues=CELERY_QUEUES
)
lg = Logger()


@app.task(name='task_demo_01')
def demo01(x, y):
    """
    name显式指定task名称
    :param x:
    :param y:
    :return:
    """
    lg.logger.info(f"当前方法名称：{sys._getframe().f_code.co_name} 当前任务id：None")
    time.sleep(10)
    return x + y


@app.task(bind=True, name='task_demo_02')
def demo02(self, x, y):
    """
    设定bind=True，可通过self将task实例传入，可获取如下信息：
        Task.name:任务名称；
        Task.request：当前任务的信息；
        Task.max_retries：设置重试的最大次数
        Task.throws：预期错误类的可选元组，不应被视为实际错误，而是结果失败；
        Task.rate_limit：设置此任务类型的速率限制
        Task.time_limit：此任务的硬限时（以秒为单位）。
        Task.ignore_result：不存储任务状态。默认False；
        Task.store_errors_even_if_ignored：如果True，即使任务配置为忽略结果，也会存储错误。
        Task.serializer：标识要使用的默认序列化方法的字符串。
        Task.compression：标识要使用的默认压缩方案的字符串。默认为task_compression设置。
        Task.backend：指定该任务的结果存储后端用于此任务。
        Task.acks_late：如果设置True为此任务的消息将在任务执行后确认 ，而不是在执行任务之前（默认行为），即默认任务执行之前就会发送确认；
        Task.track_started：如果True任务在工作人员执行任务时将其状态报告为“已启动”。默认是False；
    :param self:
    :param x:
    :param y:
    :return:
    """
    lg.logger.info(f"当前方法名称：{sys._getframe().f_code.co_name} 当前任务id：{self.request.id}")
    time.sleep(10)
    return x * y


@app.task(bind=True, name='task_demo_03')
def demo03(self, x, y):
    lg.logger.info(f"当前方法名称：{sys._getframe().f_code.co_name} 当前任务id：{self.request.id} 当前任务限时：{self.request.timelimit}")
    time.sleep(10)
    return x * y * y


def demo04(x, y):
    time.sleep(10)
    return x * y - y


@app.task(bind=True, name='task_demo_05')
def demo05(self, x, y):
    lg.logger.info(f"当前方法名称：{sys._getframe().f_code.co_name} 当前任务id：{self.request.id}")
    time.sleep(10)
    return x + y - x


# 手动绑定路由队列
@app.task(bind=True, name='task_demo_06', queue='demo06')
def demo06(self, x, y):
    lg.logger.info(f"当前方法名称：{sys._getframe().f_code.co_name} 当前任务id：{self.request.id}")
    time.sleep(10)
    return x + y - y