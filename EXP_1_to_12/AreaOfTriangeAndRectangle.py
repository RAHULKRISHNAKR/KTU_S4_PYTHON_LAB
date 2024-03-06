def tri(b,h):
    print("\nArea of Triangle: ",(b*h/2))

def rec(l,b):
    print("\nArea of Rectangle: ", l*b)


def main():
    while True:
        print("\n1.Area Of Triangle   2.Area Of Rectangle   3.Exit\n")
        choice = int(input("Enter your option : "))
        if choice == 1:
            b = int(input("Enter breadth: "))
            h = int(input("Enter height:"))
            tri(b,h)
        elif choice == 2:
            l = int(input("Enter length: "))
            b = int(input("Enter breadth: "))
            rec(l,b)
        elif choice == 3:
            break
        else:
            print("Invalid\n")

main()