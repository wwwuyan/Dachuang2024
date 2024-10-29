import json
import os
import numpy as np
import pandas as pd

from flask import request
from flask.views import MethodView
from matplotlib import pyplot as plt

from app.functions.SFRC import SFRC
from app.functions.kmeans import kmeans_clustering


class ClassificationApi(MethodView):

    def __init__(self):
        self.col_count = None
        self.row_count = None
        self.algorithm = ''

    def classification(self, data_matrix, k):
        if self.algorithm == 'kmeans':
            output = kmeans_clustering(data_matrix, k)
        if self.algorithm == 'sfrc':
            df = pd.read_csv(r"C:\Users\18365\Desktop\datasets\column_3C_weka_train_data.csv")
            y = df.iloc[:, -1].values
            X = df.iloc[:, :-1].values
            output = SFRC(X, y, data_matrix, 0.13)

        final_matrix = np.concatenate((data_matrix, output[:, np.newaxis]), axis=1)
        # 创建一个包含适当id的数组
        num_rows = final_matrix.shape[0]  # 确定矩阵的行数
        id_column = np.arange(1, num_rows + 1)[:, np.newaxis]  # 创建一个列向量，从1开始的id

        # 将id列插入到矩阵的最前面一列
        final_matrix = np.column_stack((id_column, output))

        data_json = json.dumps(final_matrix.tolist())
        return data_json, final_matrix

    def echarts(self, matrix):
        # 提取最后一列数据
        last_column = matrix[:, -1]

        # 获取最后一列的唯一值及其对应的出现次数
        unique_values, counts = np.unique(last_column, return_counts=True)

        # 将唯一值和对应的出现次数存储到两个列表中
        x_data = unique_values.tolist()
        y_data = counts.tolist()

        data = []
        for i in range(len(x_data)):
            data.append({"value": y_data[i], "name": x_data[i]})

        print(data)

        # 构建 option 对象
        option = {
            "title": {
                "text": '分类结果图',
                "left": 'center'
            },
            "tooltip": {
                "trigger": 'item'
            },
            "legend": {
                "orient": 'vertical',
                "left": 'left'
            },
            "series": [
                {
                    "name": 'Access From',
                    "type": 'pie',
                    "radius": '50%',
                    "data": data,
                    "emphasis": {
                        "itemStyle": {
                            "shadowBlur": 10,
                            "shadowOffsetX": 0,
                            "shadowColor": 'rgba(0, 0, 0, 0.5)'
                        }
                    }
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

        is_classification = request.form.get('is_classification')

        self.algorithm = request.form.get('algorithm')

        if self.algorithm is None:
            self.algorithm = 'kmeans'

        k = request.form.get('k')
        if k is not None:
            k = int(k)
        else:
            k = 3

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

        header = ["id", "分类结果"]

        header = {str(index): value for index, value in enumerate(header)}
        detail_data = json.dumps(data_matrix.tolist())
        if is_classification:
            data, matrix = self.classification(data_matrix, k)
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


classification_view = ClassificationApi.as_view('classification_api')
