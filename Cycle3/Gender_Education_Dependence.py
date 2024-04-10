'''Import necessary library:

from scipy.stats import chi2_contingency: This line imports the chi2_contingency function from the stats submodule of the scipy library. This function is used to perform a chi-squared test of independence on categorical data.
Create a contingency table:

The code defines a dictionary called data to store the observed frequencies for each category. It has three keys: "Ed Level", "Female", and "Male". The values for "Ed Level" are a list of educational levels (High School, Bachelors, Masters, Ph.D.), and the values for "Female" and "Male" are lists containing the number of females and males in each education level category.
Then, it creates a contingency table ct from the data dictionary. The contingency table is a two-dimensional array where each row represents a category of one variable, and each column represents a category of the other variable. The values in the table represent the number of observations that fall into each combination of categories. In this case, the rows represent education level and the columns represent gender.
Perform chi-squared test:

The chi2_contingency function is called with the contingency table ct as input. This function calculates the chi-squared statistic, p-value, degrees of freedom, and expected frequencies.
The chi-squared statistic is a test statistic used to assess the null hypothesis that the two variables are independent.
The p-value is the probability of observing a chi-squared statistic as extreme or more extreme than the one calculated, assuming the null hypothesis is true. A smaller p-value indicates stronger evidence against the null hypothesis.
The degrees of freedom are a statistical concept related to the number of independent comparisons being made in the analysis.
The expected frequencies are the frequencies that would be expected under the null hypothesis of independence.
Hypothesis testing:

The code performs a hypothesis test at a 5% significance level (alpha = 0.05). It checks if the p-value is less than the significance level.
If the p-value is less than 0.05, we reject the null hypothesis and conclude that there is a statistically significant dependence between gender and education level.
If the p-value is greater than or equal to 0.05, we fail to reject the null hypothesis and there is not enough evidence to conclude that gender and education level are dependent..'''

from scipy.stats import chi2_contingency
import pandas as pd

data = {
  "Ed Level": ["High School", "Bachelors", "Masters", "Ph.D.","Total"],
  "Female": [60, 54, 46, 41,201],
  "Male": [40, 44, 53, 57,194],
  "Total":[100,98,99,98,395]
}

df = pd.DataFrame(data)

print(df)
print()

ct = [data["Female"], data["Male"]]

chi2, pval, degrees_of_freedom, expected_frequency = chi2_contingency(ct)

print("Table value = 7.85\n")

print("Chi-Square Statistic:", chi2)
print()

print("Expected Frequency Table")
print(expected_frequency)
print()

print("p-value:", pval)
print()

print("Degrees of Freedom:", degrees_of_freedom)

# Hypothesis Testing at 5% significance level (alpha = 0.05)
if pval < 0.05:
    print("Reject Null Hypothesis - Gender and Education Level are dependent.")
else:
    print("Fail to Reject Null Hypothesis - Not enough evidence for dependence.")

