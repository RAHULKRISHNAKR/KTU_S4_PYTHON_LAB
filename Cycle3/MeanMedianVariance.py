'''
1. Import Library:

Import the Pandas library (pd) using import pandas as pd. This library provides data manipulation functionalities.
2. Prepare Data:

Create a list of lists named data to store the table data.
Each inner list represents a row in the table, containing elements for "State", "Population", and "Murder Rate".
Populate the data list with the values from your table.
3. Create DataFrame:

Use pd.DataFrame(data, columns=["State", "Population", "Murder Rate"]) to construct a Pandas DataFrame named df.
data: The list of lists containing the table data.
columns=["State", "Population", "Murder Rate"]: Defines the column names for the DataFrame. This step organizes the data into a structured format.
4. Calculate Mean:

Mean Population:
Use df['Population'].mean() to calculate the average population value across all states in the DataFrame.
Store the result (mean) in a variable like mean_population.
Mean Murder Rate:
Similarly, use df['Murder Rate'].mean() to calculate the average murder rate and store it in mean_murder_rate.
5. Calculate Median:

Median Population:
Use df['Population'].median() to calculate the middle value of the population data (when sorted), representing the median population.
Store the result in median_population.
Median Murder Rate:
Similarly, use df['Murder Rate'].median() to calculate the median murder rate and store it in median_murder_rate.
6. Calculate Variance:

Variance Population:
Use df['Population'].var() to calculate the population variance, which reflects how spread out the population values are from the mean.
Store the result in variance_population.
Variance Murder Rate:
Similarly, use df['Murder Rate'].var() to calculate the murder rate variance and store it in variance_murder_rate.
7. Print Results:

Print the calculated mean, median, and variance for both population and murder rate using print statements
'''

import pandas as pd
import numpy as np
# Create a list of lists to store the data
data = [
    ["Alabama", 4779736, 5.7],
    ["Alaska", 710231, 5.6],
    ["Arizona", 6392017, 4.7],
    ["Arkansas", 2915918, 5.6],
    ["California", 37253956, 4.4],
    ["Colorado", 5029196, 2.8],
    ["Connecticut", 3574097, 2.4],
    ["Delaware", 897934, 5.8],
]

df = pd.DataFrame(data, columns=["State", "Population", "Murder Rate"])

murder=[]

df["Murder"] = df["Population"]*df["Murder Rate"]
#print(df["Murder"])

x=list(df["Murder"])
for i in range(0,len(x)):
    x[i] = x[i]/100000
#print(x)

mean=np.mean(x)
med=np.median(x)
var=np.var(x)
print("Mean: ",mean)
print("Median: ",med)
print("Variance: ",var)

