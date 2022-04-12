import argparse


def parse():
    usage = "Celery Demo [options]"
    parser = argparse.ArgumentParser(prog='CELERY', usage=usage)
    parser.add_argument('-m', '--module', dest='module', action='store', required=True,
                        help='指定运行一个模块 PS:celery_basic_01')

    args = parser.parse_args()
    return args.__dict__
