import math

def vol(radius,height):
    v=math.pi*(radius**2)*height
    return v

def sa(radius,height):
    sur = 2*math.pi*radius*(radius+height)
    return sur

def main():
    r=int(input("Enter radius: "))
    h=int(input("Enter height: "))
    print("Volume: ",vol(r,h))
    print("Area: ",sa(r,h))

main()