def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def divide(a,b):
    if b==0:
        print("MATH ERROR\n")
        return
    else:
        return a/b
    
def modulo(a,b):
    return a%b
    
def main():
    while True:
        print("1.ADD   2.SUBRACT   3.MULTIPLY   4.DIVIDE   5.REMAINDER   6.EXIT")
        choice = int(input("Enter choice: "))
        if choice == 1:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result : ",add(num1,num2))
        elif choice == 2:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result : ",sub(num1,num2))
        elif choice == 3:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result : ",mul(num1,num2))
        elif choice == 4:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result : ",divide(num1,num2))
        elif choice == 5:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result : ",modulo (num1,num2))
        else: 
            break    

main()