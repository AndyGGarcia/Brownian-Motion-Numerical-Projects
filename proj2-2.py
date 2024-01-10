"""
The goal of the project is to simulate 100 paths of Brownian motion
on [0, 1] using a step size of 0.01 using the Cholesky decomposition
as outlined in Example 2.30.
"""
import random
from unicodedata import decomposition
import numpy as np
import matplotlib.pyplot as plt
#generating the covariance matrix with 0's to get the size down
cov_matrix = np.zeros((99,99))
intervals = [i*.01 for i in range(1,100)]
'''
covariance defined as min(s,t) for two times t and s
'''
#constructing the covariance matrix
for i in range(99):
    for j in range(99):
        cov_matrix[i][j] = min(intervals[i],intervals[j])
#matrix built
''''
print(cov_matrix)
now for the cholesky decomposition
'''
#using numpy function
mat_A =  np.linalg.cholesky(cov_matrix)
#defining our function to get N samples of a standard Guassian distribution
def sample_standards(N):
    sampling = []
    for i in range(N):
        sampling.append(np.random.normal(0,1))
    return sampling
"""
To generate our brownian motion B, we use B= AZ with Cholesky decomposition matrix A and
 sampled standard normal random variables Z
 Below we generate our brownian motion B on 100 intervals of length 0.01 on [0,1]
"""
#getting our sampling of standard gaussians
sampled_brownian = sample_standards(99)
#reshaping to be able to multiply an array and a matrix
#sampled_brownian = np.reshape(sampled_brownian, (99,1))
#doing out matrix multiplication
sampled_brownian = np.matmul(mat_A,sampled_brownian)
"""
#reshaping to convert back to list
sampled_brownian = np.reshape(sampled_brownian, (99,))
#back to list
"""
sampled_brownian = sampled_brownian.tolist()
#adding B0 = 0

sampled_brownian.insert(0,0)
#scaling intervals for graph
intervals = [i*100 for i in intervals]
#adding t0 = 0
intervals.insert(0,0)
#plotting graph.
'''
plt.plot(intervals,sampled_brownian)
plt.xlabel("Step number")
plt.title("Brownian Motion on [0,1] with 100 steps")
plt.show()
'''

