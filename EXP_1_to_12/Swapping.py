def method1(a,b):
    temp = a
    a = b
    b = temp

    print("After Swapping using Method 1 \nA = ",a,"   B = ",b)

def method2(a,b):
    a = a + b
    b = a - b
    a = a - b

    print("\nAfter Swapping using Method 2 \nA = ",a,"   B = ",b)

def method3(a,b):
    a,b = b,a

    print("\nAfter Swapping using Method 3 \nA = ",a,"   B = ",b)


a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
print("\nBefore Swapping = ",a,"   B = ",b,"\n")


while True:
    print("1.Use method1   2.Use method2   3.Use method3   4.Exit")
    choice = int(input("Enter choice:"))
    if choice == 1:
        method1(a,b)
    elif choice == 2:
        method2(a,b)
    elif choice == 3:
        method3(a,b)
    elif choice == 4:
        break
    else:
        print("Wrong Choice\n")

