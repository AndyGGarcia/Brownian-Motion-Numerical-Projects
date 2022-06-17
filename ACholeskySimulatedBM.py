"""
The goal of the project is to simulate paths of Brownian motion
on [0, 1] using a step size of 0.01 using the Cholesky decomposition
as outlined in Example 2.30.
"""
import random
import numpy as np
import matplotlib.pyplot as plt
class Brownian_Sampling:
    def __init__(self,num_steps):
        self.num_steps = num_steps
        self.intervals = [i*.01 for i in range(1, num_steps)]
        self.Brownian_Motion = self.ConstructBrownianPath(self.num_steps)

    def Cholesky_Decomp(self,num_steps):
        #generating the covariance matrix with 0's to get the size down
        cov_matrix = np.zeros((num_steps-1, num_steps-1))
        intervals = [i*.01 for i in range(1, num_steps)]
        '''
        covariance defined as min(s,t) for two times t and s
        '''
        #constructing the covariance matrix
        for i in range(num_steps-1):
            for j in range(num_steps-1):
                cov_matrix[i][j] = min(intervals[i], intervals[j])
        #matrix built
        ''''
        now for the cholesky decomposition
        '''
        #using numpy cholesky decomposition function to generate our Matrix A, in the equation C = AA^T
        Matrix_A = np.linalg.cholesky(cov_matrix)
        #defining our function to get N samples of a standard Guassian distribution
        return Matrix_A
    def Gaussian_Sample(self,num_steps):
        process = []
        for i in range(num_steps-1):
            process.append(np.random.normal(0, 1))
        return process
    def ConstructBrownianPath(self,num_steps):
        """
        To generate our brownian motion B, we use B= AZ with Cholesky decomposition matrix A and
        sampled standard normal random variables Z
        Below we generate our brownian motion B on 100 intervals of length 0.01 on [0,1]
        """
        #getting our sampling of standard gaussians
        Gaussian_Sample = self.Gaussian_Sample(num_steps)
        #getting our A matrix
        Matrix_A = self.Cholesky_Decomp(num_steps)
        #doing out matrix multiplication to create our Simulated Brownian Path
        Sampled_Brownian = np.matmul(Matrix_A, Gaussian_Sample)
        #back to list from np array data type
        Sampled_Brownian = Sampled_Brownian.tolist()
        #adding B0 = 0
        Sampled_Brownian.insert(0, 0)
        return self.Graph(Sampled_Brownian)

    def Graph(self,Sampled_Brownian):
        #scaling internvals for graph
        self.intervals = [i*100 for i in self.intervals]
        #adding t0 = 0
        self.intervals.insert(0, 0)
        #plotting graph.
        plt.plot(self.intervals, Sampled_Brownian)
        plt.xlabel("Step number")
        plt.title("Brownian Motion on [0,1] with {} steps".format(self.num_steps))
        plt.show()
        return
#user input to initialise our Simulation
num_steps = int(input("Enter # of steps "))
Brownian_Path = Brownian_Sampling(num_steps)
