'''Import the pandas library:

This line makes the pandas library functions available for use within the code. pandas is a powerful library for data manipulation and analysis in Python.
Create a list of data:

The code defines a list named data containing lists of values, where each inner list represents a row of data. In this case, the data includes hand lengths and heights for 5 individuals.
Create a DataFrame:

The pd.DataFrame(data, columns=["Hand", "Height"]) line constructs a DataFrame object, which is a fundamental data structure in pandas for storing and working with tabular data.
The list data is used as the data for the DataFrame, and the columns argument specifies the names of the columns to be "Hand" and "Height".
Calculate correlation coefficient:

The df.corr() line calls the corr() method on the DataFrame df. This method calculates the correlation matrix for all numerical columns in the DataFrame.
The correlation matrix is a table that shows the correlation coefficients between every pair of numerical columns.
Print the correlation matrix:

The print(correlation_matrix) line displays the calculated correlation matrix in the console. This matrix will showcase how strongly the "Hand" and "Height" variables are correlated.'''

import pandas as pd

data=[[17,150],
      [15,154],
      [19,169],
      [17,172],
      [21,175]]

df = pd.DataFrame(data, columns=["Hand","Height"])

print(df.corr())
