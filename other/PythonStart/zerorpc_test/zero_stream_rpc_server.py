import zerorpc


class StreamingRPC(object):
    @zerorpc.stream #@zerorpc.stream这里的函数修饰是必须的，否则会有异常，如TypeError: can’t serialize
    def streaming_range(self, fr, to, step):
        return range(fr, to, step)


s = zerorpc.Server(StreamingRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()