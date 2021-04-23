import jsonrpclib
import  threading


def request():
    server = jsonrpclib.ServerProxy('http://localhost:8000')
    print(server.add(2, 3))

for i in range(10):
    thread = threading.Thread(target=request)
    thread.start()

import time
time.sleep(30)