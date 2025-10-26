import numpy as np

def doolittle(A, verbose=False):

    A = np.array(A, dtype=float)
    n = A.shape[0]
    if A.shape[1] != n:
        raise ValueError("A must be square")

    L = np.zeros((n, n), dtype=float)
    U = np.zeros((n, n), dtype=float)

    for k in range(n):
        # 计算 U 的第 k 行 (j = k...n-1)
        for j in range(k, n):

            s = 0.0
            if k > 0:
                s = np.dot(L[k, :k], U[:k, j])
            U[k, j] = A[k, j] - s

        # 检查主元
        if abs(U[k, k]) < 1e-14:
            raise ValueError(f"U[{k},{k}]，太小，精度炸了")

        # 计算 L 的第 k 列 (i = k+1...n-1)
        L[k, k] = 1.0  # 单位对角
        for i in range(k + 1, n):

            s = 0.0
            if k > 0:
                s = np.dot(L[i, :k], U[:k, k])
            L[i, k] = (A[i, k] - s) / U[k, k]

        if verbose:
            print(f"k={k}:")
            print("L =\n", L)
            print("U =\n", U)


    return L, U

def forward_substitution(L, b):

    # 解 Ly = b，L 为单位下三角 (n,n)

    n = L.shape[0]
    y = np.zeros(n, dtype=float)
    for i in range(n):
        # y[i] = b[i] - sum_{j=0}^{i-1} L[i,j] * y[j]
        if i == 0:
            y[i] = b[i]
        else:
            y[i] = b[i] - np.dot(L[i, :i], y[:i])
    return y

def backward_substitution(U, y):

    # 解 Ux = y

    n = U.shape[0]
    x = np.zeros(n, dtype=float)
    for i in range(n - 1, -1, -1):

        # x[i] = (y[i] - sum_{j=i+1}^{n-1} U[i,j] * x[j]) / U[i,i]
        if i == n - 1:
            x[i] = y[i] / U[i, i]
        else:
            x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x





if __name__ == "__main__":
    A = np.array([[2, 1, 2],
                  [4, 5, 4],
                  [6, -3, 5]], dtype=float)
    b = np.array([6, 18, 5], dtype=float)

    print("原始 A =\n", A)
    print("原始 b =\n", b)

    # Doolittle 分解函数
    L, U = doolittle(A, verbose=False)

    print("L =\n", L)
    print("U =\n", U)

    # 解 Ly = b 函数
    y = forward_substitution(L, b)
    print("\n解 Ly = b 得 y =\n", y)

    # 解 Ux = y 函数
    x = backward_substitution(U, y)
    print("\n解 Ux = y 得 x =\n", x)


