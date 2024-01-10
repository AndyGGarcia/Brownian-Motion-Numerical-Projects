import numpy as np
import random as rd
import matplotlib.pyplot as plt
#choosing random seed for consistency
rd.seed(1729)
#Project 1.10
N = []
#populating N with random numbers
for i in range(0,10000):
    N.append(rd.random())
#finding probability of each number falling in each bucket


#plotting the probability density function
Our_Hist = plt.hist(N,bins = 50,range = (0,1),density = True)
plt.title("Probability Density Function")
plt.xlabel("Bin")
plt.ylabel("Frequency")
plt.show()
#Project 1.12
L = N
for i in range(10000):
    L[i] *= L[i]
Our_Histsquared = plt.hist(L, bins=50, range=(0, 1),density = True)
plt.title("Probability Density Function")
plt.xlabel("Bin")
plt.ylabel("Frequency")
plt.show()
#Project 1.13
Hist_cdf = plt.hist(N, bins=50, range=(0, 1),cumulative= True)
plt.title("Probability Cumulative Function")
plt.xlabel("Bin")
plt.ylabel("Frequency")
plt.show()
#Project 1.14
Hist_cdf_squared = plt.hist(L, bins=50, range=(0, 1),cumulative= True)
plt.title("Probability Cumulative Function")
plt.xlabel("Bin")
plt.ylabel("Frequency")
plt.show()




