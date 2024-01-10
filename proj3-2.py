"""
Use Definition3.19 to generate 10 paths of the Poisson process with rate 1
 on the interval [0, 10] with step size 0.01.
"""
import random
import numpy as np
import matplotlib.pyplot as plt
def poisson_process(rate,t,dt):
    if t == 0:
        return [0]
    total_steps = int(t/dt)
    path = [0]
    time = [0]
    for i in range(1,total_steps):
        local_t = i*dt
        parameter =rate*(local_t - (local_t-dt))
        path.append(path[i-1] + np.random.poisson(parameter))
        time.append(local_t)
    plt.plot(time,path)
    plt.show()

    return path
print(poisson_process(1,10,0.01))
