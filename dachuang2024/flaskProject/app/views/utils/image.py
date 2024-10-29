import os

from flask import send_file
from flask.views import MethodView


class ImageApi(MethodView):
    def get(self, filename):
        # 获取图片所在的目录
        current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

        # 指定资源目录的相对路径
        images_dir = os.path.join(current_dir, 'image')

        # 使用 send_file 函数发送资源
        return send_file(os.path.join(images_dir, filename))


image_view = ImageApi.as_view('image_api')
