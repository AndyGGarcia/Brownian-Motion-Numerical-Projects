'''Generating Brownian bridge off t = 1 and dt step = an input by user'''

import random
import numpy as np
import matplotlib.pyplot as plt
def Standard_B_Path(t, dt):
    """
    Returns a Standard Brownian path of length t, with steps of size dt.
    """
    if t == 0:
        return [0]
    total_steps = int(t/dt)
    path = [0]
    for i in range(1, total_steps):
        local_t = i*dt
        variance = local_t - (local_t-dt)
        path.append(path[i-1] + np.random.normal(0,np.sqrt(variance)))
    return path






def BrownianBridge(t,dt):
    B_path = Standard_B_Path(t,dt)
    total_steps = int(t/dt)
    for i in range(1,total_steps-1):
            B_path[i] = B_path[i] - B_path[-1]*(i*dt)
    B_path[-1]=0
    return B_path

#interval = float(input("Enter the time interval t value: ")) interval will always be [0,1] on brownian bridge so we dont take input
"""
Generates 100 Brownian Bridges and graphs them
"""
step_size = float(input("Enter the step size value: "))   #step_size determines how many intervals our brownian bridge will have
num_steps = int(1/step_size)
x_axis = np.linspace(0,1,num_steps) #generating an array of evenly spaced numbers on an interval to use as x axis on graph
for i in range(100):
    plt.plot(x_axis,BrownianBridge(1, step_size))
plt.show()
