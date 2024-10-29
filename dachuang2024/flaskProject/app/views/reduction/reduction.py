import json
import os
import numpy as np
import pandas as pd

from flask import request
from flask.views import MethodView

from app.functions.demo_new_Itr import MNIFS


class ReductionApi(MethodView):

    def __init__(self):
        self.col_count = None
        self.row_count = None

    def reduction(self, data_matrix, lammda):
        select_feature, sig = MNIFS(data_matrix, lammda)
        # 将两个列表组合成一个矩阵
        matrix = np.column_stack((np.array(select_feature) + 1, np.array(sig)))

        # 生成排名列数据
        new_column = np.arange(1, len(matrix) + 1)

        # 将排名列与原始矩阵连接起来
        matrix = np.column_stack((matrix, new_column))

        # 按矩阵的第一列数值从小到大排序
        sorted_matrix = matrix[matrix[:, 0].argsort()]

        data_json = json.dumps(sorted_matrix.tolist())
        return data_json, sorted_matrix

    def echarts(self, matrix):
        x_data = matrix[:, 0].tolist()
        y_data = [len(matrix[:, 2].tolist()) + 1 - data for data in matrix[:, 2].tolist()]
        # 构建 option 对象
        option = {
            "tooltip": {
                "trigger": 'axis',
                "axisPointer": {
                    "type": 'shadow'
                }
            },
            "grid": {
                "left": '3%',
                "right": '4%',
                "bottom": '3%',
                "containLabel": "true"
            },
            "xAxis": {
                "type": 'category',
                "data": x_data,
            },
            "yAxis": {
                "type": 'value',
                "name": '指标重要性',
            },
            "series": [
                {
                    "data": y_data,
                    "type": 'bar'
                }
            ]
        }

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

        is_reduction = request.form.get('is_reduction')

        lammda = request.form.get('lammda')

        if lammda is not None:
            lammda = float(lammda)
        else:
            lammda = 0.4

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

        detail_data = json.dumps(data_matrix.tolist())
        if is_reduction:
            data, matrix = self.reduction(data_matrix, lammda)
            # 生成对应的列名
            header = ["指标编号", "指标相关度", "指标约简排名"]

            header = {str(index): value for index, value in enumerate(header)}
            option = self.echarts(matrix)
            # 返回成功消息
            return {
                'status': 'success',
                'message': '分类完毕',
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


reduction_view = ReductionApi.as_view('reduction_api')
