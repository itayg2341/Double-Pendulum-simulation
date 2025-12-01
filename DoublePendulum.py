import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from DP_eval_position import DP_eval_position

# Simulation parameters
n = 5  # number of double pendulums to simulate
step = 0.01  # step size
T = np.arange(0, 10, step)  # time vector
trail = 200  # trail size

# Physical parameters
m1 = 10
m2 = 0.5
L1 = 2
L2 = 0.7
g = 9.81

# Initial conditions
d_theta1_0 = -2
d_theta2_0 = -1
theta1_0 = np.pi/2
theta2_0 = np.pi/2

phi = 0.1  # initial phase offset between each pendulum

# Initialize storage for all pendulums
x1 = np.zeros((n, len(T)))
y1 = np.zeros((n, len(T)))
x2 = np.zeros((n, len(T)))
y2 = np.zeros((n, len(T)))

# Simulate each pendulum
for i in range(n):
    initial_state = [theta1_0, theta2_0, d_theta1_0, d_theta2_0]
    x1[i], y1[i], x2[i], y2[i] = DP_eval_position(T, m1, m2, L1, L2, g, initial_state)
    theta1_0 += phi
    theta2_0 += phi

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-(L1 + L2), (L1 + L2))
ax.set_ylim(-(L1 + L2 + L2/2), L1 + L2 - L2/2)
ax.set_aspect('equal')

# Initialize plot elements
lines = []
trails1 = []
trails2 = []
masses1 = []
masses2 = []

for i in range(n):
    # Pendulum rods
    line, = ax.plot([], [], 'k-', linewidth=2)
    lines.append(line)
    
    # Trails
    trail1, = ax.plot([], [], 'r-', linewidth=1, alpha=0.5)
    trail2, = ax.plot([], [], 'b-', linewidth=1, alpha=0.5)
    trails1.append(trail1)
    trails2.append(trail2)
    
    # Masses
    mass1, = ax.plot([], [], 'ro', markersize=8, markerfacecolor='r')
    mass2, = ax.plot([], [], 'bo', markersize=8, markerfacecolor='b')
    masses1.append(mass1)
    masses2.append(mass2)

def animate(j):
    for i in range(n):
        # Update pendulum rods
        lines[i].set_data([0, x1[i, j], x2[i, j]], [0, y1[i, j], y2[i, j]])
        
        # Update trails
        start = max(0, j - trail)
        trails1[i].set_data(x1[i, start:j], y1[i, start:j])
        trails2[i].set_data(x2[i, start:j], y2[i, start:j])
        
        # Update masses
        masses1[i].set_data([x1[i, j]], [y1[i, j]])
        masses2[i].set_data([x2[i, j]], [y2[i, j]])
    
    return lines + trails1 + trails2 + masses1 + masses2

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=len(T), 
                              interval=step*1000, blit=True, repeat=True)

# Save animation to file
Writer = animation.writers['ffmpeg']
writer = Writer(fps=60, metadata=dict(artist='Double Pendulum Simulation'), bitrate=1800)
ani.save('double_pendulum.mp4', writer=writer)

plt.title('Double Pendulum Simulation')
plt.close()  # Close the figure to prevent it from showing in headless environment
print("Animation saved as 'double_pendulum.mp4'")
