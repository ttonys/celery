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
celery基本使用.

启动celery服务，`-A`指定celery应用，`worker`启动应用，`-Q`指定路由队列（默认celery）

```shell
celery -A celery_basic_01.tasks worker -l info -Q celery,demo05,demo06
```

执行主函数：

```shell
python main.py -m celery_basic_01
```

