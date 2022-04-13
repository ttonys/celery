## 开发环境
- Python==3.8
- Celery==5.2.0

## 开发配置
- 修改config.example.py为config.py
- 修改redis相关配置

## Celery不同版本对Python的支持
- Python 2.6: Celery series 3.1 or earlier.
- Python 2.5: Celery series 3.0 or earlier.
- Python 2.4: Celery series 2.2 or earlier.
- Python 2.7: Celery 4.x series.
- Python 3.6: Celery 5.1 or earlier.
- Python 3.7+: Celery 5.2.x

## 代码示例
### celery-basic-01
celery基本使用（参数绑定、任务状态查询、自动路由、手动路由等）

启动celery服务，`-A`指定celery应用，`worker`启动应用，`-Q`指定路由队列（默认celery）

```shell
celery -A celery_basic_01.tasks worker -l info -Q celery,demo05,demo06
```

执行主函数：

```shell
python main.py -m celery_basic_01
```

### celery-basic-02

celery定时任务.

启动方式01，同时下发任务与执行任务：

```
celery -A celery_basic_02.tasks worker -B -l INFO
```

启动方式02，下发任务与执行任务分离：

```
# 定时下发任务
celery -A celery_basic_02.tasks beat
```

```
# 定时执行任务
celery -A celery_basic_02.tasks worker -l INFO
```

