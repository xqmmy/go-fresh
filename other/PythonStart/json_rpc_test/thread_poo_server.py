from jsonrpclib.SimpleJSONRPCServer import PooledJSONRPCServer
from jsonrpclib.threadpool import ThreadPool

def add(a, b):
    import time
    time.sleep(1)
    return a + b

# Setup the notification and request pools
nofif_pool = ThreadPool(max_threads=10, min_threads=0)
request_pool = ThreadPool(max_threads=50, min_threads=10)

# Don't forget to start them
nofif_pool.start()
request_pool.start()

# Setup the server
server = PooledJSONRPCServer(('localhost', 8000), thread_pool=request_pool)
server.set_notification_pool(nofif_pool)

# Register methods
server.register_function(add)

#1. 超时机制 - 重试
#2. 限流 处于长期可用的状态 - 高可用
#3. 解耦
#4. 负载均衡 微服务 -分布式应用的一种具体的体现
#5. json-rpc是否满足上述的要求
#6. 序列化和反序列化数据压缩是否高效 json这种数据格式已经非常的简单了 1.这个序列化协议能将数据的压缩变得更小 2. 这个序列化和反序列化的速度够快
#json.dumps() json.loads()
#做架构 技术选型的时候 这些都是我们需要考虑到的点
#更加高效和更加全面的技术 zerorpc
#7. 这个rpc框架是否支持多语言 生态很好

try:
    server.serve_forever()
finally:
    # Stop the thread pools (let threads finish their current task)
    request_pool.stop()
    nofif_pool.stop()
    server.set_notification_pool(None)