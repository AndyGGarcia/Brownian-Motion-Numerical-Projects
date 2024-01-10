"""
For now, verify this law numeri- cally by sampling 1,000 Brownian paths
with time step 0.01 and plotting the histogram of the sample.

"""
import random
import numpy as np
import matplotlib.pyplot as plt
def B_Path(t, dt):
    """
    Returns a Brownian path of length t, with steps of size dt.
    """
    if t == 0:
        return [0]
    total_steps = int(t/dt)
    path = [0]
    time = [0]
    for i in range(1,total_steps):
        local_t = i*dt
        path.append(path[i-1] + np.random.normal(0,(local_t - (local_t-dt))**.5))
        time.append(local_t)
    return path
for i in range(100):
    plt.hist(B_Path(1,.01),100,range = (0,1),density = True)
plt.show()
