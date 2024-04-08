'''Import Libraries (Setup):

Line 1: from scipy import stats: Imports statistical functions from the SciPy library for performing the Chi-square test.
Line 2: import pandas as pd: Imports the pandas library for data manipulation. This is used to create a DataFrame from the data in the table.
2. Create DataFrame (Data Preparation):

Lines 4-8: This section defines a dictionary named data containing two lists:
"Gender": A list containing the genders (Female/Male) for each respondent.
"Education Level": A list containing the education levels (High School, Bachelors, etc.) for each respondent.
Line 9: df = pd.DataFrame(data): Creates a pandas DataFrame named df from the dictionary data. This organizes the data into a tabular format with columns representing the variables ("Gender" and "Education Level") and rows representing individual respondents.
3. Chi-Square Test (Analysis):

Line 11: stats.chi2_contingency(pd.crosstab(df["Gender"], df["Education Level"])): Performs the Chi-square test of independence using chi2_contingency from SciPy.
pd.crosstab(df["Gender"], df["Education Level"]): This part calculates the contingency table, which shows the frequency counts for each combination of gender and education level.
Line 11 (Output): This line outputs four values and stores them in separate variables:
chi2_statistic: The Chi-square statistic, a measure of the discrepancy between observed and expected frequencies (assuming independence).
p_value: The probability of observing a Chi-square statistic as extreme or more extreme, assuming the null hypothesis (gender and education level are independent) is true.
expected_frequency: A table containing the expected frequencies for each cell in the contingency table if the variables were independent.
observed_frequency: A table containing the observed frequencies for each cell in the contingency table (the data from your table).
4. Print Results (Output):

Line 12: print("Chi-square statistic:", chi2_statistic): Prints the calculated Chi-square statistic value.
Line 13: print("p-value:", p_value): Prints the calculated p-value.
5. Interpretation (Optional):

Line 14: alpha = 0.05: Sets the significance level (alpha) commonly used for hypothesis testing (usually 0.05). This represents the maximum acceptable probability of rejecting the null hypothesis due to random chance.
Lines 15-18: An if-else statement interprets the p-value based on the chosen alpha level:
if p_value <= alpha: If the p-value is less than or equal to alpha, the code rejects the null hypothesis. This indicates a statistically significant association between gender and education level.
else: If the p-value is greater than alpha, the code fails to reject the null hypothesis. There's not enough evidence to conclude a statistically significant dependence between gender and education level at the chosen significance level.'''

from scipy import stats
import pandas as pd

# Create a DataFrame from the data in the table
data = {
    "Gender": ["Female", "Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Male"],
    "Education Level": ["High School", "Bachelors", "Masters", "Ph.D.", "High School", "High School", "Bachelors", "Masters", "Ph.D.", "Bachelors", "High School", "Bachelors", "Masters", "Bachelors", "High School", "Masters", "Bachelors", "Ph.D.", "High School", "Masters"]
}

df = pd.DataFrame(data)

# Chi-square test for independence
chi2_statistic, p_value, expected_frequency, observed_frequency = stats.chi2_contingency(pd.crosstab(df["Gender"], df["Education Level"]))

# Print the results
print("Chi-square statistic:", chi2_statistic)
print("p-value:", p_value)

# Interpretation
alpha = 0.05
if p_value <= alpha:
    print("Reject null hypothesis. Gender and Education Level are dependent at the 5%% significance level.")
else:
    print("Fail to reject null hypothesis. Gender and Education Level are not dependent at the 5%% significance level.")
