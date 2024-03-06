from datetime import datetime, timedelta

def countdown(target_date):
  """
  Calculates the time remaining until a target date.

  Args:
    target_date: The date to count down to, as a datetime object.

  Returns:
    A string representing the time remaining until the target date, in the format
    "X days, Y hours, Z minutes, and W seconds".
  """

  # Get the current date and time.
  now = datetime.now()

  # Calculate the difference between the target date and the current date.
  time_remaining = target_date - now

  # Extract the days, hours, minutes, and seconds from the time remaining.
  days = time_remaining.days
  hours = time_remaining.seconds // 3600
  minutes = (time_remaining.seconds % 3600) // 60
  seconds = time_remaining.seconds % 60

  # Format the output string.
  output = ""
  if days > 0:
    output += f"{days} days, "
  if hours > 0:
    output += f"{hours} hours, "
  if minutes > 0:
    output += f"{minutes} minutes, and "
  output += f"{seconds} seconds"

  return output

# Set the target date.
target_date = datetime(2024, 2, 24, 0, 0, 0)  # Replace with your desired date

# Calculate and print the countdown.
countdown_str = countdown(target_date)
print(countdown_str)
