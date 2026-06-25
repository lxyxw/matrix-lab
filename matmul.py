import numpy as np
def matmul_python(A, B):
    m = len(A)
    k = len(A[0])
    n = len(B[0])
    # 初始化一个 m 行 n 列的零矩阵
    C = [[0 for _ in range(n)] for _ in range(m)]    
    # 三重循环计算矩阵乘法
    for i in range(m):
        for j in range(n):
            s = 0
            for t in range(k):
                s += A[i][t] * B[t][j]
            C[i][j] = s           
    return C
def matmul_numpy(A, B):
    A = np.array(A)
    B = np.array(B)
    return A @ B
def test_matmul():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    C_python = matmul_python(A, B)
    C_numpy = matmul_numpy(A, B)
    assert C_python == [[19, 22], [43, 50]]
    assert np.array_equal(C_numpy, np.array([[19, 22], [43, 50]]))
    print("All tests passed")
if __name__ == "__main__":
    test_matmul()

