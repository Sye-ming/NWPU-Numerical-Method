import numpy as np

# 系数矩阵 A 与常数项 b
A = np.array([[10, -2, -1],
              [-2, 10, -1],
              [-1, -2,  5]], dtype=float)
b = np.array([3, 15, 10], dtype=float)

# 提取 D, L, U
D = np.diag(np.diag(A))
L = np.tril(A, -1)
U = np.triu(A, 1)

# 预计算 (D + L)^{-1}
DL_inv = np.linalg.inv(D + L)

# 初始向量
x = np.zeros(3)
epsilon = 1e-3
max_iter = 200

print(f'初始向量 x^0 = {x}')

for k in range(max_iter):
    x_old = x.copy()

    # Gauss–Seidel 定义形式：x^{k+1} = (D+L)^{-1} (b - Ux^{k})
    x = DL_inv.dot(b - U.dot(x_old))

    print(f'第{k+1}次迭代: x^{k+1} = {x}')

    if np.linalg.norm(x - x_old, np.inf) < epsilon:
        print(f'\n迭代在第{k+1}次停止，|x^(k+1) - x^(k)| < {epsilon}')
        break

print(f'\n最终近似解: {x}')
