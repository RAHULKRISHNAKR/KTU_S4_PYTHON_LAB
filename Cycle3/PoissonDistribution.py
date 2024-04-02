'''
1. Import Library:

The program starts by importing the math library using import math. This library provides mathematical functions like factorial and exp (exponential) that are used in the Poisson probability formula.
2. Define Function:

A function named poisson_probability is defined. This function takes two arguments:
lambda_param: This is a float representing the rate parameter (mean) of the Poisson distribution.
k: This is an integer representing the number of occurrences you're interested in calculating the probability for.
3. Docstring (Optional):

The function includes a docstring (the lines in triple quotes """ ... """) that explains the function's purpose and the meaning of its arguments and return value. This improves code readability and maintainability.
4. Calculate Probability:

Inside the function, the following steps are performed to calculate the probability:
probability = (math.exp(-lambda_param) * (lambda_param**k)) / math.factorial(k): This line calculates the probability using the Poisson probability formula.
math.exp(-lambda_param): Calculates the exponential term (e raised to the power of negative lambda_param).
(lambda_param**k): Raises lambda_param to the power of k.
math.factorial(k): Calculates the factorial of k.
The entire expression divides the exponential term by the factorial of k to get the probability.
5. Return Probability:

The line return probability returns the calculated probability value from the function. This value can be used by the code that calls the function.
6. Example Usage:

'''

import math

def poisson_probability(lambda_param, k):
  # Calculate the probability using the Poisson probability formula
  probability = (math.exp(-lambda_param) * (lambda_param**k)) / math.factorial(k)
  return probability

# Example usage:
lambda_param = 3.4  # Rate parameter of the Poisson distribution
k = 6  # Number of occurrences we're interested in

# Calculate the probability
probability = poisson_probability(lambda_param, k)
print("Probability of", k, "occurrences:", probability)
