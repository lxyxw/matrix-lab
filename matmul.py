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