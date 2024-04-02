'''1. Import Libraries:

numpy: This library provides functions for numerical computations, including generating sequences of numbers.
matplotlib.pyplot: This library offers tools for creating visualizations like plots.
2. Define plot_graph function:

This function takes three arguments:
x: An array of x-axis values.
y: An array of corresponding y-axis values.
label: A string representing the function being plotted.
It creates a new plot figure using plt.figure().
It then plots the data points using plt.plot(x, y, 'r-', label=label). Here, 'r-' specifies a red continuous line.
The function sets labels for the x and y-axis using plt.xlabel and plt.ylabel.
It adds a title to the plot using plt.title(label).
Legends are created using plt.legend() to differentiate between plots if multiple functions are visualized.
A grid is added for better readability with plt.grid(True).
Finally, the plot is displayed on the screen using plt.show().
3. Main Program Loop:

The program displays a menu offering choices for different functions to plot (y = x, y = x^2, etc.).
It enters a loop using while True.
Inside the loop, the user's choice is retrieved using input("Enter your choice: ").
A series of if-elif statements handle each choice:
If the choice is a valid number between 1 and 6:
It defines appropriate ranges for the x-axis using np.linspace.
It calculates the corresponding y-axis values based on the chosen function (e.g., y = x**2 for choice 2).
The plot_graph function is called with the generated data and function label.
If the choice is '7':
An exit message is printed.
The loop is broken using break.'''

import numpy as np
import matplotlib.pyplot as plt

def plot_graph(x, y, label):
    plt.figure()
    plt.plot(x, y,'r-',label=label)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(label)
    plt.legend()
    plt.grid(True)
    plt.show()

print("Choose a function to plot:")
print("1. y = x")
print("2. y = x^2")
print("3. y = 2^x")
print("4. y = sin(x)")
print("5. y = cos(x)")
print("6. y = e^x")
print("7. Exit")


while True:

	choice = input("Enter your choice: ")

	if choice == '1':
		x = np.linspace(-10, 10, 400)
		y = x
		plot_graph(x, y, "y = x")
	elif choice == '2':
		x = np.linspace(-10, 10, 400)
		y = x**2
		plot_graph(x, y, "y = x^2")
	elif choice == '3':
		x = np.linspace(-2, 2, 400)
		y = 2**x
		plot_graph(x, y, "y = 2^x")
	elif choice == '4':
		x = np.linspace(-2*np.pi, 2*np.pi, 400)
		y = np.sin(x)
		plot_graph(x, y, "y = sin(x)")
	elif choice == '5':
		x = np.linspace(-2*np.pi, 2*np.pi, 400)
		y = np.cos(x)
		plot_graph(x, y, "y = cos(x)")
	elif choice == '6':
		x = np.linspace(-2, 2, 400)
		y = np.exp(x)
		plot_graph(x, y, "y = e^x")
	elif choice == '7':
		print("Exiting...")
		break
	else:
		print("Invalid choice. Please enter a number between 1 and 7.")
