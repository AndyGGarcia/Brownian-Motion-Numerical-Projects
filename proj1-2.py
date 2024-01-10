from cmath import inf
import numpy as np
import random as rd
import matplotlib.pyplot as plt
#project 1.20 Law of Large numbers
#populating K with random numbers
K = []
n = 1000
x = [1/(i+1) for i in range(n)]
xaxis = [i for i in range(n)]
for i in range(n):
    K.append(rd.random())
cumsum  = np.cumsum(K) #cumsum array
for i in range(len(cumsum)):
    cumsum[i] = cumsum[i]*x[i]
y = cumsum
plt.plot(xaxis,y)
plt.title("Law of Large Numbers")
plt.xlabel("Number of elements")
plt.ylabel("Mean")
plt.show()
def EMean(l):
    N = len(K)
    cumsum = np.cumsum(K)  # cumsum array
    for i in range(len(cumsum)):
        cumsum[i] = cumsum[i]/(i+1)
    return cumsum

