import requests
import logging
import time
from random import randint
from jaeger_client import Config


def download():
    rsp = requests.get("https://www.imooc.com")
    return rsp


def parser():
    time.sleep(randint(1, 9) * 0.1)


def insert_to_mysql(parent_span):
    #1. 生成sql的时间
    with tracer.start_span('prepare', child_of=parent_span) as prepare_span:
        time.sleep(randint(1, 9) * 0.1)

    #2. 插入数据库的时间
    with tracer.start_span('execute', child_of=parent_span) as execute_span:
        time.sleep(randint(1, 9) * 0.1)


if __name__ == "__main__":
    log_level = logging.DEBUG
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(asctime)s %(message)s', level=log_level)

    config = Config(
        config={ # usually read from some yaml config
            'sampler': {
                'type': 'const', #全部
                'param': 1, #1 开启全部采样 0 表示关闭全部采样
            },
            'local_agent': {
              'reporting_host':'192.168.0.104',
              'reporting_port': '6831',
            },
            'logging': True,
        },
        service_name='mxshop',
        validate=True,
    )
    # this call also sets opentracing.tracer
    tracer = config.initialize_tracer()

    with tracer.start_span("spider") as spider_span:

        #下载
        with tracer.start_span('get', child_of=spider_span) as get_span:
            download()

        #解析
        with tracer.start_span('parser', child_of=spider_span) as parser_span:
            parser()

        # 入库
        with tracer.start_span('insert', child_of=spider_span) as insert_span:
            insert_to_mysql(insert_span)

    time.sleep(2)   # yield to IOLoop to flush the spans - https://github.com/jaegertracing/jaeger-client-python/issues/50
    tracer.close()  # flush any buffered spans