def large(a,b,c):
    largest = a
    if(b>largest):
        largest=b
    if(c>largest):
        largest=c
    return largest

def main():
    a = int(input("Enter A"))
    b = int(input("Enter B"))
    c = int(input("Enter C"))
    print("Largest is",large(a,b,c))

main()