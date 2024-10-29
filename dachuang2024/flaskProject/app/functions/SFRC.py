import numpy as np
import torch
from sklearn.preprocessing import MinMaxScaler
from torch.nn.functional import pairwise_distance


def soft_distance(x, Di, C):
    tensor_x = torch.tensor(x)
    dist_arr = []
    result = []
    for sample in Di:
        tensor_sample = torch.tensor(sample)
        dist = pairwise_distance(tensor_x, tensor_sample)
        dist_arr.append(dist)
    # 将张量转换为常规的 Python 列表
    dist_arr = [tensor.item() for tensor in dist_arr]

    # 对列表进行排序
    dist_arr.sort()
    for i in range(len(dist_arr)):
        result.append(dist_arr[i] - i * C)

    # 将 result 转换为 NumPy 数组
    result_np = np.array(result)
    # 获取最大值的索引
    max_index = np.argmax(result_np)

    return dist_arr[max_index]


def SFRC(training_samples, training_labels, test_sample, C):
    # 归一化特征
    scaler = MinMaxScaler()
    training_samples = scaler.fit_transform(training_samples)
    test_sample = scaler.transform(test_sample)
    labels = []
    classnum = np.max(training_labels) - np.min(training_labels) + 1

    for i in range(test_sample.shape[0]):
        degree = []
        for class_label in range(0, classnum):
            class_data = training_samples[training_labels != class_label]
            degree.append(soft_distance(test_sample[i], class_data, C=C))
        # print(degree)
        class_star = np.argmax(degree)
        labels.append(class_star)

    # 将数字标签映射为文字标签
    # label_map = {0: "正常", 1: "椎间盘突出", 2: "脊柱滑脱"}
    label_map = {0: "正常", 1: "心肌炎", 2: "冠心病"}

    # 将数字标签转换为文字标签
    labeled_data = np.array([label_map[label] for label in labels])

    return labeled_data
