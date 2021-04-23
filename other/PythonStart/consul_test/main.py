import requests

headers = {
    "contentType":"application/json"
}


def register(name, id, address, port):
    url = "http://192.168.1.103:8500/v1/agent/service/register"
    print(f"http://{address}:{port}/health")
    rsp = requests.put(url, headers=headers, json={
        "Name":name,
        "ID":id,
        "Tags":["mxshop", "bobby", "imooc", "web"],
        "Address":address,
        "Port":port,
        "Check": {
            "GRPC":f"{address}:{port}",
            "GRPCUseTLS": False,
            "Timeout": "5s",
            "Interval": "5s",
            "DeregisterCriticalServiceAfter": "15s"
        }
    })
    if rsp.status_code == 200:
        print("注册成功")
    else:
        print(f"注册失败：{rsp.status_code}")


def deregister(id):
    url = f"http://192.168.1.103:8500/v1/agent/service/deregister/{id}"
    rsp = requests.put(url, headers=headers)
    if rsp.status_code == 200:
        print("注销成功")
    else:
        print(f"注销失败：{rsp.status_code}")


def filter_service(name):
    url = "http://192.168.1.103:8500/v1/agent/services"
    params = {
        "filter": f'Service == "{name}"'
    }
    rsp = requests.get(url, params=params).json()
    for key, value in rsp.items():
        print(key)


if __name__ == "__main__":
    # register("mshop-web", "mshop-web", "192.168.1.102", 50051)
    # deregister("mshop-web")
    filter_service("user-srv")
