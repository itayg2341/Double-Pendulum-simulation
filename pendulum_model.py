import numpy as np

def pendulum_model(state, t, m1, m2, L1, L2, g, u=0):
    """
    System model for double pendulum
    state = [theta1, theta2, d_theta1, d_theta2]
    Returns angular accelerations [d2_theta1, d2_theta2]
    """
    theta1, theta2, d_theta1, d_theta2 = state
    
    a11 = (m1 + m2) * L1**2
    a12 = m2 * L1 * L2 * np.cos(theta1 - theta2)
    b1 = m2 * L2 * L1 * d_theta2**2 * np.sin(theta2 - theta1) - (m1 + m2) * g * L1 * np.sin(theta1) + u * L1 * np.cos(theta1)
    
    a21 = m2 * L2 * L1 * np.cos(theta1 - theta2)
    a22 = m2 * L2**2
    b2 = -m2 * L1 * L2 * np.sin(theta2 - theta1) * d_theta1**2 - m2 * g * L2 * np.sin(theta2) + u * L2 * np.cos(theta2)
    
    A = np.array([[a11, a12], [a21, a22]])
    B = np.array([b1, b2])
    
    theta_vett = np.linalg.solve(A, B)
    return theta_vett
