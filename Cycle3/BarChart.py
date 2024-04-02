'''1. Import Libraries:

Import the Matplotlib library for plotting with the line import matplotlib.pyplot as plt.
2. Prepare Data:

Create two lists:
continents: a list containing the names of continents.
areas: a list holding the corresponding areas of each continent in millions of square miles.
3. Create Bar Chart:

Initialize figure: Use plt.figure(figsize=(10, 6)) to create a figure for the plot and set its dimensions.
Generate bar chart: Use plt.bar(continents, areas, color=[colors]) to create the bar chart, specifying:
continents for the x-axis labels.
areas for the bar heights.
color (optional) for a list of colors to assign to each bar.
4. Add Labels and Title:

Label axes: Use plt.xlabel("Continents") and plt.ylabel("Area (Million Square Miles)") to label the x and y axes, respectively.
Set title: Use plt.title("Areas of Continents (Million Square Miles)") to provide a descriptive title for the plot.
5. Customize Visuals (Optional):

Add data labels: Use plt.text(x, y, value, ha='center', va='bottom') for each bar to display data labels above the bars:
x represents the horizontal position of the label.
y represents the vertical position of the label.
value is the value to be displayed.
ha='center' aligns the label horizontally centered within the bar.
va='bottom' aligns the label along the bottom of the bar.
Rotate x-axis labels: Use plt.xticks(rotation=45) to rotate x-axis labels for better readability if they overlap.
Add grid lines: Use plt.grid(axis='y', linestyle='--', alpha=0.7) to add grid lines to the y-axis, enhancing interpretation.
6. Display Plot:

Adjust spacing: Use plt.tight_layout() to automatically adjust spacing between elements for a neater appearance.
Show plot: Use plt.show() to display the generated bar chart.
_______________________________________________________________________________________________________________________________

'''

# Import libraries
import matplotlib.pyplot as plt

# Continent names and their corresponding areas (in millions of square miles)
continents = ["Africa", "Asia", "Europe", "North America", "Oceania", "South America", "Soviet Union"]
areas = [11.7, 10.4, 1.9, 9.4, 3.3, 6.9, 7.9]

# Create a bar chart
plt.figure(figsize=(10, 6))  # Adjust figure size for better visualization
plt.bar(continents, areas, color=['green', 'blue', 'orange', 'red', 'purple', 'yellow', 'gray'])
plt.xlabel("Continents")
plt.ylabel("Area (Million Square Miles)")
plt.title("Areas of Continents (Million Square Miles)")

# Add data labels above bars (optional)
for i, v in enumerate(areas):
    plt.text(i, v + 0.1, f"{v:.1f}", ha='center', va='bottom')  # Adjust offset for data labels

# Rotate x-axis labels for better readability (optional)
plt.xticks(rotation=45)

# Show the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid lines for better readability
plt.tight_layout()  # Adjust spacing between elements
plt.show()
