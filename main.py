import celery_basic_01
import celery_basic_02
from celery_basic_01 import run
from celery_basic_02 import run
from utils.parser import parse
from utils.logger import Logger

lg = Logger()

if __name__ == "__main__":
    cmd_parse = parse()
    if cmd_parse["module"] == "celery_basic_01":
        lg.logger.info(f'run module {cmd_parse["module"]}')
        celery_basic_01.run.main()
    elif cmd_parse["module"] == "celery_basic_02":
        lg.logger.info(f'run module {cmd_parse["module"]}')
        celery_basic_02.run.main()
    else:
        lg.logger.error("指定模块无效")
