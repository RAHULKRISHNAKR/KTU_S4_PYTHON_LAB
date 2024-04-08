''' Import Library:

from scipy import stats: This line imports the statistical functions (stats) from the SciPy library, making them available for use.
2. Sample Data:

mpg = [21, 22, 23, 20, ...]: This line defines a list named mpg containing the sample fuel mileage data for the 16 light trucks. You'll need to replace this with your actual data in practice.
3. Hypothesized Mean:

mu = 20: This line sets the mu variable to the hypothesized population mean, which is the average fuel mileage of the previous light truck model we're comparing to.
4. Perform t-test:

t_stat, p_value = stats.ttest_1samp(mpg, mu): This line performs the one-sample t-test using the stats.ttest_1samp function from SciPy.
It takes two arguments:
mpg: The list containing the sample fuel mileage data.
mu: The hypothesized population mean (previous model's MPG).
The function calculates two values and stores them in separate variables:
t_stat: The t-statistic, which measures how far the sample mean deviates from the hypothesized mean.
p_value: The p-value, which indicates the probability of observing a t-statistic as extreme or more extreme, assuming the null hypothesis (no significant difference in fuel mileage) is true.
5. Print Results:

print("t-statistic:", t_stat): This line prints the calculated t-statistic value.
print("p-value:", p_value): This line prints the calculated p-value.'''

from scipy import stats

# Sample data (replace with your actual data)
mpg = [21, 22, 23, 20, 24, 25, 19, 21, 22, 20, 23, 21, 22, 24, 20, 21]

# Hypothesized population mean (replace with the previous model's MPG)
mu = 20

# Perform a one-sample t-test
t_stat, p_value = stats.ttest_1samp(mpg, mu)

# Print the results
print("t-statistic:", t_stat)
print("p-value:", p_value)

# Interpretation
alpha = 0.05
if p_value <= alpha:
  print("Reject null hypothesis. The new model has a significantly different fuel mileage compared to the previous model (p < ", alpha, ").")
else:
  print("Fail to reject null hypothesis. There is no significant difference in fuel mileage between the new model and the previous model (p > ", alpha, ").")
