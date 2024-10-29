# -*- coding = utf-8 -*-
# @Time : 2023/7/24
# @Author : wuyan
# @File : KFRAD.py
# @Software : PyCharm

import numpy as np
import xlrd
from scipy.io import loadmat
from scipy.spatial.distance import pdist, squareform


# Kernelized fuzzy rough anomaly detection(KFRAD)

# 计算关系矩阵的函数：输入属性子集数据和核参数，输出模糊关系矩阵
# data需是矩阵类型,多属性子集是矩阵类型
# 单属性子集可用list矩阵化后转置:temp=gaussian_matrix((np.matrix(a[:,0])).T,r)或者 temp=gaussian_matrix(a[:,0:1],r)
def gaussian_matrix(data, r):
    n = data.shape[0]  # 获取矩阵行数，n个样本
    m = data.shape[1]  # 获取矩阵列数，m个属性
    datatrans = np.zeros((n, m))
    datatrans[:, 0:m] = data
    temp = pdist(datatrans, 'euclidean')  # 计算欧式距离
    temp = squareform(temp)
    temp = np.exp(-(temp ** 2) / r)  # 用核函数求隶属度
    return temp


# input:
# data is data matrix without decisions, where rows for samples and columns for attributes.
# lammda is used to adjust the adaptive fuzzy radius.
# output:
# Ranking objects and fuzzy rough granules-based outlier factor (FRGOF)

def KFRAD(data, delta):
    n, m = data.shape

    # 计算第一个条件属性的邻域集合 -------------------------------
    LA = np.arange(0, m)  # 属性集合序号0~m-1，对应1~m
    weight1 = np.zeros((n, m))  # 单属性权重
    weight3 = np.zeros((n, m))  # 单属性权重

    Acc_A_a = np.zeros((n, m))  # 去掉一个属性之后的近似精度
    for l in range(0, m):
        lA_d = np.setdiff1d(LA, l)  # 在LA中但不在l中的已排序的唯一值
        # Acc_A_a_tem = np.zeros((n, m))

        # 求单属性子集的模糊关系矩阵
        NbrSet_tem = gaussian_matrix((np.matrix(data[:, l])).T, delta)
        NbrSet_temp, ia, ic = np.unique(NbrSet_tem, return_index=True, return_inverse=True, axis=0)
        # ia为矩阵NbrSet_temp中的元素在矩阵NbrSet_tem中的位置
        # ic为矩阵NbrSet_tem中的元素在矩阵NbrSet_temp中的位置
        # NbrSet_temp去除了NbrSet_tem的重复元素并升序排列

        for i in range(0, NbrSet_temp.shape[0]):  # NbrSet_temp的行数
            i_tem = np.where(ic == i)[0]

            data_tem = data[:, lA_d]
            NbrSet_tmp = gaussian_matrix(data_tem, delta)  # 多属性子集的模糊关系矩阵

            a = 1 - NbrSet_tmp
            b = np.tile(NbrSet_temp[i, :], (n, 1))
            Low_A = sum((np.minimum(a + b - np.multiply(a, b) + np.multiply(np.sqrt(2 * a - np.multiply(a, a)),
                                                                            np.sqrt(2 * b - np.multiply(b, b))),
                                    1)).min(-1))

            a = NbrSet_tmp
            Upp_A = sum((np.maximum(
                np.multiply(a, b) - np.multiply(np.sqrt(1 - np.multiply(a, a)), np.sqrt(1 - np.multiply(b, b))),
                0)).max(-1))

            Acc_A_a[i_tem, l] = Low_A / Upp_A  # 计算近似精度

            weight3[i_tem, l] = 1 - (sum(NbrSet_temp[i, :]) / n) ** (1 / 3)
            weight1[i_tem, l] = (sum(NbrSet_temp[i, :]) / n)

    GAL = np.zeros((n, m))
    for col in range(m):
        GAL[:, col] = 1 - (Acc_A_a[:, col]) * weight1[:, col]

    KFRAD = np.array(np.mean(GAL * weight3, axis=1))
    KFRAD = np.round(KFRAD, 3)
    return KFRAD


# min-max-normalize----------------------------------------------
# start,end是归一化的列范围
# 注意：此处start,end的取值在1~m之间
def normalize(data, start, end):
    n = data.shape[0]  # 获取矩阵行数
    m = data.shape[1]  # 获取矩阵列数
    trandata = np.zeros((n, m - 1))
    if start < 1 or end > m or start > end:
        print("范围出错")
    else:
        for i in range(start - 1, end):
            temp = data[:, i]
            max = np.max(temp)
            min = np.min(temp)
            if (max > 1):
                dis = max - min
                temp = (temp - min) / dis
            trandata[:, i] = temp
    return trandata
