import os

import pandas as pd
from flask import request
from flask.views import MethodView


class FileApi(MethodView):
    def sum(self, file):
        try:
            # 使用 Pandas 读取 excel 文件
            df = pd.read_excel(file)

            # 提取第一列数据并求和
            result = df.iloc[:, 1 - 1].sum()

            return result
        except Exception as e:
            print("An error occurred:", str(e))
            return None

    def post(self):
        # 检查是否有文件上传
        if 'file' not in request.files:
            return {
                'status': 'error',
                'message': 'No file provided',
                'code': 1
            }

        # 获取上传的文件
        file = request.files['file']

        # 检查文件是否存在
        if file.filename == '':
            return {
                'status': 'error',
                'message': 'No file selected',
                'code': 2
            }

        total_sum = self.sum(file)

        # 指定相对路径保存文件，相对于当前工作目录
        upload_folder = 'file'

        # 获取当前工作目录
        current_directory = os.getcwd()

        print(upload_folder, "+", current_directory, "+", total_sum)
        # 构建保存文件的完整路径
        save_path = os.path.join(current_directory, upload_folder, file.filename)

        # 保存文件
        file.save(save_path)
        total_sum = int(total_sum)

        # 返回保存成功的消息
        return {
            'status': 'success',
            'message': 'Sum calculated successfully',
            'sum': total_sum
        }


file_view = FileApi.as_view('file_api')
