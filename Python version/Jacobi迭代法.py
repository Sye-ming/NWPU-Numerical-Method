import numpy as np

A = np.array([[ 5,  2,  1],
              [-1,  4,  2],
              [ 2, -3, 10]], dtype=float)
b = np.array([-12, 20, 3], dtype=float)

x = np.array([-3., 1., 1.])      # 初始向量
tol = 1e-3
max_iter = 200

print(f'初始向量 x^0 = {x}')

for k in range(max_iter):

    x_new = np.zeros(3)
    x_new[0] = (b[0] - A[0,1]*x[1] - A[0,2]*x[2]) / A[0,0]
    x_new[1] = (b[1] - A[1,0]*x[0] - A[1,2]*x[2]) / A[1,1]
    x_new[2] = (b[2] - A[2,0]*x[0] - A[2,1]*x[1]) / A[2,2]

    print(f'第{k+1}次迭代 x^{k+1} = {x_new}')


    if np.linalg.norm(x_new - x, np.inf) < tol:
        print(f'\n迭代在第{k+1}次停止，‖x^{k+1} - x^{k}‖∞ < {tol}')
        break
    x = x_new.copy()

print(f'\n最终近似解: {x_new}')