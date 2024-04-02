'''
1. Define the function:

Identify the mathematical relationship between y and x.
Write a Python function f(x) that expresses this relationship. This function will take an x value as input and return the corresponding y value.
2. Set plotting range and resolution:

Decide on the minimum (start) and maximum (end) values for the x-axis that you want to visualize in the graph.
Choose the number of data points (num) you want to generate for the x-axis. More data points will result in a smoother curve.
3. Generate x-axis values:

Use numpy.linspace(start, end, num) to create an array of num x-axis values that are equally spaced between start and end.
4. Calculate corresponding y values:

Iterate through the x-axis values array.
For each x value, call the f(x) function to calculate the corresponding y value.
Store these y values in a separate array.
5. Create the plot using Matplotlib:

Import the matplotlib.pyplot library as plt.
Use plt.plot(x, y) to create a line plot, where x is the array of x-axis values and y is the array of corresponding y values.
6. Customize the plot (optional):

Add labels to the axes using plt.xlabel("X-axis") and plt.ylabel("Y-axis").
Set a title for the plot using plt.title("Graph of y = f(x)").
7. Display the plot:
Use plt.show() to display the generated graph.
'''


import matplotlib.pyplot as plt
import numpy as np

# Define the function
def f(x):
  return x**2

# Generate x values
x = np.linspace(-2, 2, 100)

# Calculate y values
y = f(x)

# Plot the graph
plt.plot(x, y)

# Set labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Plot of y = x^2")

# Show the plot
plt.grid(True)
plt.show()
