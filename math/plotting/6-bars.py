#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# Define the labels and colors for each type of fruit
people = ['Farrah', 'Fred', 'Felicia']
apples = fruit[0]
bananas = fruit[1]
oranges = fruit[2]
peaches = fruit[3]

# Plot the stacked bars
plt.bar(people, apples, width=0.5, color='red', label='Apples')
plt.bar(people, bananas, width=0.5, bottom=apples, color='yellow', label='Bananas')
plt.bar(people, oranges, width=0.5, bottom=apples + bananas, color='#ff8000', label='Oranges')
plt.bar(people, peaches, width=0.5, bottom=apples + bananas + oranges, color='#ffe5b4', label='Peaches')

# Set the y-axis label and title
plt.ylabel('Quantity of Fruit', fontsize='x-small')
plt.title('Number of Fruit per Person', fontsize='x-small')

# Set the y-axis range and ticks
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))

# Add a legend
plt.legend(loc='upper right', fontsize='x-small')

# Show the plot
plt.show()
