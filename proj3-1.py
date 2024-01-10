"""Simulating Brownian motion using increments.
    Use the definition of Brownian motion in Proposition 3.1 to construct
  a function def in Python that takes as inputs the time interval and the step size and
  yields as an output a Brownian path.
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
        path.append(path[i-1] +  np.random.normal(0,np.sqrt(local_t- (local_t-dt))))
        time.append(local_t)
    plt.plot(time,path)
    plt.show()
    return path
interval = int(input("Enter the time interval t value: "))
step_size = float(input("Enter the step size value: "))
ourpath = B_Path(interval, step_size)
print(ourpath)

