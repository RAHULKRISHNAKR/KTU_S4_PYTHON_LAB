string = input("Enter word:")
string=string.lower()

if (string==string[::-1]):
    print("Is a palindrome")
else:
    print("Is not a palindrome")
