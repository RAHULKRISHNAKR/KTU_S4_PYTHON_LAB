def is_armstrong(number):
    if number <= 0:
        return False

    # Count the number of digits
    num_digits = len(str(number))

    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10

    return number == sum_of_powers


def is_prime(n):
    if n <= 1:
        return False  # Handle non-positive and 1

    # Special cases for 2 and 3
    if n <= 3:
        return True

    # Check for divisibility by 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Optimized loop for even divisibility check
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def main():
    number = int(input("Enter a number to check amstrong and prime: "))
    if is_armstrong(number) and is_prime(number):
        print("Both Amstrong and prime")
    elif is_armstrong(number):
        print("Armstrong Number")
    elif is_prime(number):
        print("Prime Number")
    else:
        print("Neither prime nor composite")

main()