import json
from urllib.parse import urlparse, parse_qsl
from http.server import HTTPServer, BaseHTTPRequestHandler

host = ('', 8003)

#将url映射到对应的函数 urlconfig route call id的映射
#反序列化
class AddHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        qs = dict(parse_qsl(parsed_url.query))
        a = int(qs.get("a", 0))
        b = int(qs.get("b", 0))
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({
            "result":a+b
        }).encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(host, AddHandler)
    print("启动服务器")
    server.serve_forever()
