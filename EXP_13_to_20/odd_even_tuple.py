numbers = input("Enter numbers separated by commas: ")
mytuple = tuple([int(num) for num in numbers.split(",")])

enum = [num for num in mytuple if num % 2 == 0]
print("Even numbers:", enum)

onum = [num for num in mytuple if num % 2 != 0]
print("Odd numbers:", onum)

eindice = [mytuple[i] for i in range(len(mytuple)) if i % 2 == 0]
print("Numbers at even indices:", eindice)

oindice = [mytuple[i] for i in range(len(mytuple)) if i % 2 != 0]
print("Numbers at odd indices:", oindice)
