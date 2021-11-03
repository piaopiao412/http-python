
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
from flask import request


data = {'result': 'hello, this is python http server!'}
host = ('192.168.203.83', 8888)



class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        print(self.headers)
        print(self.command)
        req_datas = self.rfile.read(int(self.headers['content-length']))
        # print(type(req_datas))
        req_datas.decode('ISO-8859-1')
        self.send_response(500)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('ISO-8859-1'))
        # self.wfile.write(req_datas.encode('ISO-8859-1'))

        upload_file = request.files['files']

        # 获取图片名
        file_name = upload_file.filename


        # 文件保存目录（桌面）
        file_path = r'/home/hq/TestFile'
        if upload_file:
            # 地址拼接
            file_paths = os.path.join(file_path, file_name)
            # 保存接收的图片到桌面
            upload_file.save(file_paths)
            # 随便打开一张其他图片作为结果返回，
            return 'file success'
        return 'file fail'

server = HTTPServer(host, Resquest)
print("Starting server, listen at: %s:%s" % host)
server.serve_forever()
