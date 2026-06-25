import numpy as np
import time
import random
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


def random_matrix(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]


def benchmark():
    sizes = [32, 64, 128]
    print("size, python_time, numpy_time")
    for n in sizes:
        A = random_matrix(n)
        B = random_matrix(n)
        start = time.perf_counter()
        matmul_python(A, B)
        python_time = time.perf_counter() - start
        start = time.perf_counter()
        matmul_numpy(A, B)
        numpy_time = time.perf_counter() - start
        print(n, python_time, numpy_time)

if __name__ == "__main__":
    test_matmul()
    benchmark()