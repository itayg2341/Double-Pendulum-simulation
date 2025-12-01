import numpy as np
from scipy.integrate import odeint
from pendulum_model import pendulum_model

def DP_eval_position(T, m1, m2, L1, L2, g, initial_state):
    """
    Simulates the position (cartesian coordinates) of the two masses
    T: time vector
    Returns: x1, y1, x2, y2 trajectories
    """
    def system(state, t):
        return np.concatenate([
            state[2:],  # d_theta1, d_theta2
            pendulum_model(state, t, m1, m2, L1, L2, g)  # d2_theta1, d2_theta2
        ])
    
    out = odeint(system, initial_state, T)
    theta1 = out[:, 0]
    theta2 = out[:, 1]
    
    x1 = L1 * np.sin(theta1)
    x2 = L1 * np.sin(theta1) + L2 * np.sin(theta2)
    y1 = -L1 * np.cos(theta1)
    y2 = -L2 * np.cos(theta2) - L1 * np.cos(theta1)
    
    return x1, y1, x2, y2
