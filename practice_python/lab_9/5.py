import numpy as np
from scipy.stats import multivariate_normal
import time


def log_density(X, m, C):
    D = len(m)
    det = np.linalg.det(C)
    inv = np.linalg.inv(C)
    diff = X - m
    exponent = -0.5 * np.sum(diff.dot(inv) * diff, axis=1)
    normalization = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det)
    log = exponent + normalization
    return log


N = 5
D = 10
X = np.random.randn(N, D)
m = np.random.randn(D)
C = np.random.randn(D, D)
C = np.dot(C, C.T)

start1 = time.time()
log = log_density(X, m, C)
print(log)
final1 = time.time()-start1


start2 = time.time()
log2 = multivariate_normal(m, C).logpdf(X)
print(log2)
final2 = time.time()-start2

print(f'Время выполнения своей функции: {final1}')
print(f'Время выполнения с помощью scipy.stats.multivariate_normal: {final2}')
