'''Generating Brownian bridge off t = 100 and dt step == 1'''

import random
from threading import local
import numpy as np
import matplotlib.pyplot as plt
def Standard_B_Path(t, dt):
    """
    Returns a Brownian path of length t, with steps of size dt.
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

#interval = float(input("Enter the time interval t value: ")) will always be 1 on brownian bridge
step_size = float(input("Enter the step size value: "))
for i in range(100):
    plt.plot(BrownianBridge(1, step_size))
plt.show()
