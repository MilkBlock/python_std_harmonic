import numpy as np
m = np.array([[0,1],[1,1]])
mx4 = np.linalg.matrix_power(m,4)
start = np.matrix([0,1]).T
np.matmul(mx4,start)
