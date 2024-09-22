import numpy as np

def gauss(a, b, n, tol):
    # Initialization of variables
    s = np.zeros(n)
    x = np.zeros(n)
    er = 0

    # Scaling factor for each row
    for i in range(n):
        s[i] = abs(a[i][0])
        for j in range(1, n):
            if abs(a[i][j]) > s[i]:
                s[i] = abs(a[i][j])

    er = eliminate(a, s, n, b, tol)

    if er != -1:
        x = substitute(a, n, b)

    return x, er

def eliminate(a, s, n, b, tol):
    for k in range(n - 1):
        pivot(a, b, s, n, k)
        if abs(a[k][k] / s[k]) < tol:
            return -1  # Error code for singular matrix or division by zero

        for i in range(k + 1, n):
            factor = a[i][k] / a[k][k]
            for j in range(k + 1, n):
                a[i][j] -= factor * a[k][j]
            b[i] -= factor * b[k]

    if abs(a[n-1][n-1] / s[n-1]) < tol:
        return -1

    return 0  # Successful elimination

def pivot(a, b, s, n, k):
    p = k
    big = abs(a[k][k] / s[k])

    for ii in range(k + 1, n):
        dummy = abs(a[ii][k] / s[ii])
        if dummy > big:
            big = dummy
            p = ii

    if p != k:
        # Swap rows p and k in matrix a
        for jj in range(k, n):
            a[p][jj], a[k][jj] = a[k][jj], a[p][jj]
        
        # Swap corresponding elements in vector b
        b[p], b[k] = b[k], b[p]
        
        # Swap the scaling factors
        s[p], s[k] = s[k], s[p]

def substitute(a, n, b):
    x = np.zeros(n)
    x[n-1] = b[n-1] / a[n-1][n-1]

    for i in range(n-2, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum += a[i][j] * x[j]
        x[i] = (b[i] - sum) / a[i][i]

    return x

# Example usage
a = np.array([[2.0, -1.0, 0.0],
              [-1.0, 2.0, -1.0],
              [0.0, -1.0, 2.0]])

b = np.array([1.0, 0.0, 1.0])

n = len(b)
tol = 1e-9

x, er = gauss(a, b, n, tol)

if er == 0:
    print("Solution:", x)
else:
    print("No unique solution found due to numerical instability.")
