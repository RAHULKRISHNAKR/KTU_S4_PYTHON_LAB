'''
1. Import Library:

Import the math library for mathematical functions like factorial using import math.
2. Define Functions:

binomial_probability(trials, probability_of_success, successes):

This function takes three arguments:
trials: The number of independent trials in the binomial experiment.
probability_of_success: The probability of success in each trial.
successes: The number of successes you're interested in calculating the probability for.
The function calculates the probability using the binomial probability formula and returns the result. The formula considers the number of trials, probability of success for each trial, and the desired number of successes.
probability_at_least_one_success(trials, probability_of_success):

This function takes two arguments:
trials: The number of independent trials in the binomial experiment.
probability_of_success: The probability of success in each trial.
It calculates the probability of having at least one success in trials attempts.
It calculates the probability of zero successes (no successes) using binomial_probability(trials, probability_of_success, 0).
It subtracts the probability of zero successes from 1 to get the probability of having at least one success (since these are complementary events).
3. Calculate Probability of Specific Successes:

Set the number of trials (trials), probability of success in each trial (probability_of_success), and the number of successes you want the probability for (successes).
Call the binomial_probability function with these values to calculate the probability of getting that specific number of successes in the given number of trials.
4. Calculate Probability of At Least One Success:

Set the number of trials (trials) and probability of success in each trial (probability_of_success).
Call the probability_at_least_one_success function with these values to calculate the probability of having at least one success in the given number of trials.
5. Print Results:

Print separate messages indicating the probability of getting the specified number of successes and the probability of having at least one sucess
'''

import math

def binomial_probability(trials, probability_of_success, successes):
  # Calculate the probability using the binomial probability formula
  probability = (math.factorial(trials) / (math.factorial(successes) * math.factorial(trials - successes))) * (probability_of_success**successes) * ((1 - probability_of_success) ** (trials - successes))
  return probability

def probability_at_least_one_success(trials, probability_of_success):

  # Probability of at least 1 success is 1 minus the probability of 0 successes
  probability_no_success = binomial_probability(trials, probability_of_success, 0)
  probability_at_least_one_success = 1 - probability_no_success
  return probability_at_least_one_success

# Example usage:
trials = 6  # Number of trials
probability_of_success = 0.25  # Probability of success in each trial

# Calculate probability of 4 successes
successes = 4
probability = binomial_probability(trials, probability_of_success, successes)
print("Probability of", successes, "successes in", trials, "trials:", probability)

# Calculate probability of at least 1 success
probability_at_least_one_success = probability_at_least_one_success(trials, probability_of_success)
print("Probability of at least 1 success in", trials, "trials:", probability_at_least_one_success)
