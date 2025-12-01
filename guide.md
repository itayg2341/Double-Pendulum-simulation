# Double Pendulum Simulation Guide

This guide explains how to run and use the Python double pendulum simulation that was converted from MATLAB.

## Requirements

The simulation requires the following Python packages:
- numpy
- matplotlib
- scipy

You can install them using pip:
```bash
pip install numpy matplotlib scipy
```

## Running the Simulation

To run the simulation, execute the main script:
```bash
python DoublePendulum.py
```

This will:
1. Simulate 5 double pendulums with slightly different initial conditions
2. Display an animated visualization showing:
   - Black rods representing the pendulum arms
   - Red circles for the first mass
   - Blue circles for the second mass
   - Red and blue trails showing the recent path of each mass

## How It Works

### Core Components

1. **pendulum_model.py**: Contains the physics equations for the double pendulum system
   - Implements the system of differential equations
   - Calculates angular accelerations based on current state
   - Uses numpy for matrix operations

2. **DP_eval_position.py**: Handles the simulation and position calculations
   - Uses scipy.integrate.odeint to solve the differential equations
   - Converts angular positions to Cartesian coordinates
   - Returns trajectories for both masses

3. **DoublePendulum.py**: Main script that sets up and runs the simulation
   - Configures simulation parameters (masses, lengths, initial conditions)
   - Runs multiple simulations with slightly different initial conditions
   - Creates animated visualization using matplotlib

### Key Parameters

You can modify these parameters in DoublePendulum.py:
- `n`: Number of pendulums to simulate
- `step`: Time step size (smaller = smoother but slower)
- `T`: Total simulation time
- `trail`: Length of the trail behind each mass
- `m1, m2`: Masses of the two pendulum bobs
- `L1, L2`: Lengths of the two pendulum rods
- `g`: Gravitational acceleration
- `theta1_0, theta2_0`: Initial angles
- `d_theta1_0, d_theta2_0`: Initial angular velocities
- `phi`: Phase offset between pendulums

### Physics Model

The simulation uses the following physics assumptions:
- Masses are located at the extremities (rods are massless)
- Rotational friction is zero
- The system is governed by the coupled differential equations in pendulum_model.py

### Visualization

The animation shows:
- Real-time motion of multiple pendulums
- Trails indicating recent path history
- Different colors for each mass (red for first, blue for second)
- Equal aspect ratio to maintain physical proportions

## Tips

1. For smoother animation, decrease the step size (but this will increase computation time)
2. To see more chaotic behavior, increase the initial angles or velocities
3. To compare sensitivity to initial conditions, adjust the phase offset `phi`
4. For longer trails, increase the `trail` parameter
5. To save the animation, you can modify DoublePendulum.py to use matplotlib's animation saving capabilities

## Troubleshooting

1. If the animation is slow, try:
   - Increasing the step size
   - Reducing the number of pendulums
   - Decreasing the trail length

2. If the animation doesn't appear:
   - Make sure you have all required packages installed
   - Check that matplotlib is configured to display plots
   - Try running with `python -i DoublePendulum.py` to keep the window open

## Comparison with MATLAB

The Python version produces the same chaotic behavior as the original MATLAB version:
- Same sensitivity to initial conditions
- Same visualization style (colors, trails, etc.)
- Same physics model and parameters
- Similar animation smoothness
