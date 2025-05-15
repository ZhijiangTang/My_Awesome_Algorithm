import numpy as np

def n_sum_exact(B, n, m):
    # 初始生成函数 (常数多项式1)
    G = np.array([1])

    # 遍历数组B的每个元素，构造生成函数并进行多项式相乘
    for i in range(len(B)):
        max_exponent = m // B[i]  # 只需要关心 x^m 以内的项
        # 构造几何级数 (1 + t*x^B[i] + t^2*x^2B[i] + ... )
        poly = np.zeros(max_exponent * B[i] + 1)
        for j in range(1, max_exponent + 1):
            poly[j * B[i]] = 1  # 选取 j 次 B[i]，使得指数为 j*B[i]

        # 多项式卷积求生成函数乘积
        G = np.convolve(G, poly)

        # 为了节省空间，只保留 x^m 的项
        if len(G) > m:
            G = G[:m+1]

    # 检查 t^n * x^m 的系数
    if len(G) > m and G[m] > 0:
        return True
    else:
        return False

# 示例使用
B = [1, 3, 5, 7]
n = 2
m = 4  # 目标和
result = n_sum_exact(B, n, m)
print("是否存在选取恰好 n 个元素和为 m 的组合: ", result)
