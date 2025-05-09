#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3
x = np.arange(0, 11)

# Plot y as a solid red line
plt.plot(x, y, 'r-', label='y = x^3')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line graph of y = x^3')

# Display the legend
plt.legend()

# Show the plot
plt.show()
