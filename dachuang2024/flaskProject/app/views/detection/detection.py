import json
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from flask import request
from flask.views import MethodView

from app.functions.KFRAD import KFRAD


class DetectionApi(MethodView):

    def __init__(self):
        self.col_count = None
        self.row_count = None
        self.result = None
        self.n = ''

    def detection(self, data_matrix, delta):
        output = KFRAD(data_matrix, delta)
        self.result = output

        final_matrix = np.concatenate((data_matrix, output[:, np.newaxis]), axis=1)
        # 创建一个包含适当id的数组
        num_rows = final_matrix.shape[0]  # 确定矩阵的行数
        id_column = np.arange(1, num_rows + 1)[:, np.newaxis].astype(int)  # 创建一个列向量，从1开始的id

        # 创建异常列
        anomalies = ["存在异常" if value > self.n else "暂无风险" for value in output]

        # 将id列插入到矩阵的最前面一列
        final_matrix = np.column_stack((id_column, output, anomalies))

        data_json = json.dumps(final_matrix.tolist())
        return data_json

    def echarts(self):
        # 使用列表推导式生成 scatter_data 列表
        scatter_data = [[i + 1, value] for i, value in enumerate(self.result)]
        if self.n != '':
            linevalue = self.n
        else:
            linevalue = 0
        # 构建 option 对象
        option = {
            "xAxis": {},
            "yAxis": {},
            "series": [
                {
                    "symbolSize": 10,
                    "data": scatter_data,
                    "type": "scatter",
                    "markLine": {
                        "symbol": ["none"],
                        "silent": True,
                        "lineStyle": {
                            "type": "solid",
                            "color": "red"
                        },
                        "label": {
                            "position": "middle"
                        },
                        "data": [
                            {
                                "yAxis": linevalue
                            }
                        ]
                    }
                }
            ]
        }

        # 将 Python 字典转换为 JSON 字符串
        # json_string = json.dumps(option, indent=2)

        # 输出 JSON 字符串
        return option

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

        self.n = request.form.get('n')
        if self.n is not None:
            self.n = float(self.n)
        else:
            self.n = 0.4

        is_detection = request.form.get('is_detection')

        delta = request.form.get('delta')
        if delta is not None:
            delta = float(delta)

        # 检查文件是否存在
        if file.filename == '':
            return {
                'status': 'error',
                'message': 'No file selected',
                'code': 2
            }
        # 指定相对路径保存文件，相对于当前工作目录
        upload_folder = 'file'

        # 获取当前工作目录
        current_directory = os.getcwd()

        # 构建保存文件的完整路径
        save_path = os.path.join(current_directory, upload_folder, file.filename)

        # 保存文件
        file.save(save_path)

        # 从CSV文件中加载数据到DataFrame
        data_frame = pd.read_csv(save_path, encoding='utf-8', header=None)

        self.row_count = data_frame.shape[0]
        self.col_count = data_frame.shape[1] - 1

        data_matrix = data_frame.values

        data_matrix = np.delete(data_matrix, data_matrix.shape[1] - 1, axis=1)  # 删除最后一列

        # 获取列的数量
        num_columns = len(data_frame.columns) - 1

        # 生成对应的列名
        detail_header_column = [f'指标{i}' for i in range(1, num_columns + 1)]

        detail_header = {str(index): value for index, value in enumerate(detail_header_column)}

        header = ["id", "异常分数", "检测结果"]

        header = {str(index): value for index, value in enumerate(header)}
        detail_data = json.dumps(data_matrix.tolist())
        if is_detection:
            data = self.detection(data_matrix, delta)
            option = self.echarts()
            # 返回成功消息
            return {
                'status': 'success',
                'message': '检测完毕',
                'data': data,
                'header': header,
                'option': option,
            }
        else:
            # 返回成功消息
            return {
                'status': 'success',
                'message': '上传完成',
                'row_count': self.row_count,
                'col_count': self.col_count,
                'file': file.filename,
                'detail_data': detail_data,
                'detail_header': detail_header
            }


detection_view = DetectionApi.as_view('detection_api')
