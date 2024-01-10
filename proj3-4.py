"""
ConsideraOrnstein-Uhlenbeckprocess on [0, 1], (𝑋𝑡 , 𝑡 ∈ [0, 1]) as
in Numerical Project 2.3. Repeat the experiment of Project 3.3 with
Ornstein-Uhlenbeck paths. What do you notice?
"""
import random
import numpy as np
import matplotlib.pyplot as plt
import math
def B_Path(t, dt):
    """
    Returns a Brownian path of length t, with steps of size dt.
    """
    if t == 0:
        return [0]
    total_steps = int(t/dt)
    path = [0]
    time = [0]
    for i in range(1, total_steps):
        local_t = i*dt
        var =((math.exp(-2*(local_t - (local_t-dt))))/2) * (1 - math.exp(-2*(local_t-dt)))
        path.append(path[i-1] + np.random.normal(0,var))
        time.append(local_t)
    return path


for i in range(100):
    plt.hist(B_Path(1, .01), 100, range=(0, 1), density=True)
plt.show()
