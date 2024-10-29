import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def kmeans_clustering(data, num_clusters):
    """
    使用 K-means 算法进行聚类

    参数：
    - data: 包含要进行聚类的数据的二维数组
    - num_clusters: 聚类簇的数量

    返回：
    - labels: 每个样本所属的聚类标签
    - centroids: 聚类中心点的坐标
    """
    # 数据归一化
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # 创建 K-means 聚类器
    kmeans = KMeans(n_clusters=num_clusters)

    # 执行聚类
    kmeans.fit(scaled_data)

    # 获取聚类标签
    labels = kmeans.labels_

    # 将数字标签映射为文字标签
    label_map = {0: "正常", 1: "椎间盘突出", 2: "脊柱滑脱"}

    # 将数字标签转换为文字标签
    labeled_data = np.array([label_map[label] for label in labels])

    return labeled_data
