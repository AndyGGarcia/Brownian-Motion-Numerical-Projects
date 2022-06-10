"""Simulating Brownian motion using increments.
    Use the definition of Brownian motion in Proposition 3.1 to construct
  a function def in Python that takes as inputs the time interval and the step size and
  yields as an output a Brownian path.
"""
import random
import numpy as np
import matplotlib.pyplot as plt
def Brownian_Path(t, dt):
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
    return path
interval = float(input("Enter the time interval t value: "))
step_size = float(input("Enter the step size value: "))
num_paths = int(input("Enter the number of paths you would like to simulate: "))
num_steps = int(interval/step_size)
x_axis = np.linspace(0, interval, num_steps)
for i in range(num_paths):
    plt.plot(x_axis, Brownian_Path(interval, step_size))
plt.show()
