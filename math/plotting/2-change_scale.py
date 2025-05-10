#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# Plot x ↦ y as a line graph
plt.plot(x, y, 'r-', label='C-14 Decay')

# Set the x-axis and y-axis labels
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')

# Set the title of the graph
plt.title('Exponential Decay of C-14')

# Set the y-axis to logarithmic scale
plt.yscale('log')

# Add grid for better readability (optional)
plt.grid(True)

# Show the plot
plt.show()
