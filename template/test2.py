import base64
from flask import request
from flask import Flask
import os

app=Flask(__name__)

# 定义路由
@app.route("/photo", methods=['POST'])
def get_frame():
    # 接收图片
    upload_file = request.files['file']
    upload_form = request.files['text']
    # 获取图片名
    file_name = upload_file.filename
    form_name = upload_form.formname


    # 文件保存目录（桌面）
    file_path=r'/home/hq/TestFile'
    if upload_file:
        # 地址拼接
        file_paths = os.path.join(file_path, file_name)
        # 保存接收的图片到桌面
        upload_file.save(file_paths)
        # 随便打开一张其他图片作为结果返回，
        return 'file success'


    if upload_form:
        form_paths = os.path.join(file_path, form_name)
        # 保存接收的图片到桌面
        upload_form.save(form_paths)
        # 随便打开一张其他图片作为结果返回，
        return 'form success'
    else:
        return 'form fail'
        # with open(r'C:/Users/Administrator/Desktop/1001.jpg', 'rb') as f:
        #     res = base64.b64encode(f.read())
        #     return res




if __name__ == "__main__":
    app.run('192.168.203.83', port=8888)