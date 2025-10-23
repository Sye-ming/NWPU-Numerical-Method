import numpy as np

A = np.array([[3, -4, 3],
              [-4, 6, 3],
              [3, 3, 1]], dtype=float)

V_0 = np.array([1., 1., 1.])
epsilon = 1e-7

lambda_list = []

i = 0
V_standard = V_0.copy()          # 当前单位特征向量
print(f"{i}\t{V_standard}\t N/A")

# 第一次迭代
V = A @ V_standard
lam = np.linalg.norm(V, np.inf)
V_standard = V / lam
lambda_list.append(lam)
i += 1
print(f"{i}\t{V}\t{V_standard}\t{lam}")

# 第二次迭代
V = A @ V_standard
lam = np.linalg.norm(V, np.inf)
V_standard = V / lam
lambda_list.append(lam)
i += 1
print(f"{i}\t{V}\t{V_standard}\t{lam}")

# 继续迭代
while abs(lambda_list[-1] - lambda_list[-2]) > epsilon:
    V = A @ V_standard
    lam = np.linalg.norm(V, np.inf)
    V_standard = V / lam
    lambda_list.append(lam)
    i += 1
    print(f"{i}\t{V}\t{V_standard}\t{lam}")

print("\n主特征值 λ =", lambda_list[-1])
print("对应特征向量 =", V_standard)