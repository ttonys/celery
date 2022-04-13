# -*- coding: utf-8 -*-
# @Time    : 2022/4/12 4:10 下午
# @FileName: config.py
# @Software: PyCharm
from kombu import Queue, Exchange

# redis基本配置信息
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_PASS = "123456"
REDIS_DB_BROKER = 0
REDIS_DB_BACKEND = 1

"""celery常见配置参数
注意: celery4.0对配置参数进行了修改，但在celery6.0之前依然支持读取旧的配置文件
参考: https://docs.celeryq.dev/en/stable/userguide/configuration.html
"""
# celery消息队列地址
CELERY_BROKER = f'redis://:{REDIS_PASS}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB_BROKER}'
# celery任务状态或结果存储地址
CELERY_BACKEND = f'redis://:{REDIS_PASS}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB_BACKEND}'
# celery任务序列化方式
CELERY_TASK_SERIALIZER = 'json'
# celery处理序列化方式
CELERY_RESULT_SERIALIZER = 'json'
# celery指定任务接收的序列化类型
CELERY_ACCEPT_CONTENT = ['json']
# celery压缩方案zlib或bzip2，默认不压缩
CELERY_MESSAGE_COMPRESSION = 'zlib'
# celery任务发送是否需要确认
CELERY_ACKS_LATE = True
# celery任务执行时间限制，超时会被kill
CELERYD_TASK_TIME_LIMIT = 5
# celery最大任务并发数，默认内核数量，超过最大并发会任务在PENDING状态
CELERYD_CONCURRENCY = 4
# celery-worker执行了多少任务就会死掉，默认无限制
CELERYD_MAX_TASKS_PER_CHILD = 40
# celery默认队列名称
CELERY_DEFAULT_QUEUE = "default"
# celery时区配置，issues:https://github.com/celery/celery/issues/4842
CELERY_TIMEZONE = "Asia/Shanghai"
# celery是否使用utc时区
CELERY_ENABLE_UTC = False
# celery手动路由定义
CELERY_QUEUES = (
    Queue('demo06', Exchange("demo06"), routing_key='demo06'),
)
CELERY_ROUTES = {
    "celery_basic_01.tasks.demo06": {"queue": "demo06", "routing_key": "demo06"}
}
# celery定时任务配置
CELERY_BEAT_SCHEDULE = {
    'cycle-30-seconds': {
        'task': 'beat_demo01',
        'schedule': 30.0,
        'args': (16, 16)
    },
}