import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist, squareform


# 计算模糊多粒度熵
def entropy(M):
    a = M.shape[0]
    K = sum(-(1 / a) * (np.log2(1 / (M.sum(axis=0)))))
    return K


# 计算关系矩阵
def rela_srr(data, delta):
    datatrans = np.zeros((len(data), 2))
    datatrans[:, 0] = data
    temp = pdist(datatrans, 'cityblock')  # 计算曼哈顿距离，差的绝对值
    temp = squareform(temp)  # 把得到的一维矩阵转化为二维矩阵
    # temp[temp > (1 - delta)] = 1
    temp[temp > delta] = 1
    r = 1 - temp
    return r


# 算法的主要实现
def MNIFS(data, lammda):
    # 获取data的行列数，row:对象数，attrinu:属性数
    row, attrinu = data.shape

    # delta是属性的多邻域半径
    delta = np.zeros(attrinu)

    ID = (data <= 1).all(axis=0)
    delta[ID] = (np.std(data[:, ID], axis=0)) / lammda

    Select_Fea = []  # 已被选择的特征
    sig = []  # 用于记录每个特征被选择时的指标值

    E = np.zeros(attrinu)  # E是模糊多粒度熵
    Joint_E = np.zeros((attrinu, attrinu))  # Joint_E是模糊多粒度联合熵
    MI = np.zeros((attrinu, attrinu))  # MI是模糊互信息

    # 计算模糊多粒度熵
    for j in range(0, attrinu):
        r = rela_srr(data[:, j], delta[j])  # r是属性j对应的模糊多邻域颗粒
        E[j] = entropy(r)

    # print("模糊多粒度熵：")
    # print(E)

    # 计算模糊多粒度联合熵和模糊互信息
    for i in range(0, attrinu):
        ri = rela_srr(data[:, i], delta[i])  # ri是属性i对应的模糊集
        for j in range(0, i + 1):
            rj = rela_srr(data[:, j], delta[j])  # rj是属性j对应的模糊集
            Joint_E[i, j] = entropy(np.minimum(ri, rj))  # 计算i和j的联合熵
            Joint_E[j, i] = Joint_E[i, j]
            # i和j的模糊互信息等于i和j的模糊多粒度熵之和减去i和j的模糊联合熵
            MI[i, j] = E[i] + E[j] - Joint_E[i, j]
            MI[j, i] = MI[i, j]

    # print('模糊多粒度联合熵：')
    # print(Joint_E)
    #
    # print('模糊互信息FMI：')
    # print(MI)

    # 计算模糊相关性，即模糊互信息的平均值
    Ave_MI = np.mean(MI, axis=1)  # 计算每一行的均值

    n1 = (np.argsort(Ave_MI)[::-1]).tolist()  # 排序后的索引值
    x1 = (Ave_MI[np.argsort(Ave_MI)[::-1]]).tolist()  # 排序后的Ave_MI

    # print("模糊相关性:")
    # print(Ave_MI)

    sig.append(x1[0])
    Select_Fea.append(n1[0])
    unSelect_Fea = n1[1:]

    # 计算未被选择的特征的冗余度
    while unSelect_Fea:
        Red = np.zeros((len(unSelect_Fea), len(Select_Fea)))  # Red：冗余度
        # i是未选择特征
        for i in range(0, len(unSelect_Fea)):
            # j是已选择特征
            for j in range(0, len(Select_Fea)):
                # FE = Joint_E[Select_Fea[j], unSelect_Fea[i]] - E[unSelect_Fea[i]]
                FE = Joint_E[Select_Fea[j], unSelect_Fea[i]]
                Red[i, j] = Ave_MI[Select_Fea[j]] - FE / E[Select_Fea[j]] * Ave_MI[Select_Fea[j]]

        Ave_FRed = np.mean(Red, axis=1)  # 计算每个未选择特征对应的冗余度平均值

        # print('冗余度：')
        # print(Ave_FRed)

        # 计算交互性
        Itr = np.zeros((len(unSelect_Fea), len(unSelect_Fea)))  # Itr:交互性

        # 如果只剩一个未选择特征，则交互性为0
        if len(unSelect_Fea) == 1:
            Ave_Itr = np.sum(Itr, axis=1)
        else:
            # 使用交点法计算关系矩阵
            srrcj = np.ones((row, row))
            for j in range(0, len(Select_Fea)):
                srr_Select_j = rela_srr(data[:, Select_Fea[j]], delta[Select_Fea[j]])
                srrcj = np.minimum(srrcj, srr_Select_j)
            # 遍历所有未选特征，计算当前候选特征c的交互性
            for c in range(0, len(unSelect_Fea)):
                # 遍历所有未选特征
                for i in range(0, len(unSelect_Fea)):
                    if c == i:
                        continue
                    # 计算交互性，使用公式I[p;q|t]=Joint_E[p,t]+Joint_E[q,t]-Joint_E[p,q,t]-E[t]
                    srr_UnSe_i = rela_srr(data[:, unSelect_Fea[i]], delta[unSelect_Fea[i]])
                    srr_UnSe_c = rela_srr(data[:, unSelect_Fea[c]], delta[unSelect_Fea[c]])
                    Joint_Three = entropy(np.minimum(np.minimum(srr_UnSe_i, srrcj), srr_UnSe_c))
                    Joint_Two = entropy(np.minimum(srrcj, srr_UnSe_c))
                    Itr[c, i] = Joint_E[unSelect_Fea[i], unSelect_Fea[c]] + Joint_Two - Joint_Three - E[unSelect_Fea[c]]
                    Itr[c, i] = np.abs(Itr[c, i])
                    # print(Joint_E[unSelect_Fea[i], unSelect_Fea[c]] ,Joint_Two , Joint_Three , E[unSelect_Fea[c]])
                    # print(Itr[c, i],'c:',c,'i:',i)

            # print(Itr)
            Ave_Itr = np.sum(Itr, axis=1)
            Ave_Itr = Ave_Itr / (len(unSelect_Fea) - 1)

            # print('交互性：')
            # print(Ave_Itr)

        # 计算最大相关最小冗余最大交互
        UFmRMR = Ave_MI[unSelect_Fea] - Ave_FRed + Ave_Itr
        UFmRMR = UFmRMR.tolist()
        # print('评价指标：')
        # print(UFmRMR)
        max_sig = max(UFmRMR)
        max_tem = UFmRMR.index(max(UFmRMR))
        sig.append(max_sig)
        Select_Fea.append(unSelect_Fea[max_tem])
        unSelect_Fea.pop(max_tem)

    select_feature = Select_Fea

    # print('相关度是：', sig)
    # print('特征序列：', select_feature)
    return select_feature, sig
