import socketserver
import http.server
import logging
import cgi
from flask import request
import requests
import json , base64 , cv2
import numpy as np
from http.server import HTTPServer, BaseHTTPRequestHandler
PORT = 8888


class ServerHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.error(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.error(self.headers)
        form = cgi.FieldStorage(

                                fp=self.rfile,
                                headers = self.headers,
                                environ = {'REQUEST_METHOD':'POST',
                                           'CONTENT_TYPE':self.headers['Content-type']
                                            }
                                )
        # print(form)

        # for item in form.list:
        #     logging.error(item)
        # http.server.SimpleHTTPRequestHandler.do_GET(self)
        # with open("date.txt", 'w') as file:
        #     for key in form.keys():
        #         file.write(str(form.getvalue(str(key))) + ',')
        #         # self.wfile.write("GET request for {}".format(self.path).encode('ISO-8859-1'))
        #         fn = file.decode('utf-8', 'ignore').strip('\x00')
        # with open(form, 'rb') as f:
        #     data = f.read()



Handler = ServerHandler
httpd = socketserver.TCPServer(('192.168.203.83', PORT), Handler)
print("server at port", PORT)
httpd.serve_forever()
upload_file = request.get_data()
req = json.loads(upload_file)
# old_file_name = upload_file.filename

if upload_file:
    name = req['data']
    print(name)
    img_str = req['files']  # 得到unicode的字符串
    img_decode_ = img_str.encode('ascii')  # 从unicode变成ascii编码
    img_decode = base64.b64decode(img_decode_)  # 解base64编码，得图片的二进制
    img_np_ = np.frombuffer(img_decode, np.uint8)
    img = cv2.imdecode(img_np_, cv2.COLOR_RGB2BGR)  # 转为opencv格式
    # cv2.imshow('frame', img)
    # cv2.imwrite('./', newimg)
    cv2.waitKey()
    cv2.imwrite('img.bmp', img)

    # cv2.waitKey()

