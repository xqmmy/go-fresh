import consul

c = consul.Consul(host="192.168.1.103")

address = "192.168.1.102"
port = 50051
check={
    "GRPC":f"{address}:{port}",
    "GRPCUseTLS": False,
    "Timeout": "5s",
    "Interval": "5s",
    "DeregisterCriticalServiceAfter": "15s"
}

# rsp = c.agent.service.register(name="user-srv", service_id="user-srv2",
#                          address=address, port=port, tags=["mxshop"],check=check)
rsp = c.agent.services()
for key, val in rsp.items():
    rsp = c.agent.service.deregister(key)
# print(rsp)
