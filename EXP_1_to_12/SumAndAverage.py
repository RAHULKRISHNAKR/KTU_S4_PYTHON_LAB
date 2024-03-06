'''Write a program to read n students name and mark of three subjects
    Calculate Sum & Average of marks and Print result'''

class Student:
    def __init__(self,name,m1,m2,m3):
        self.name = name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def compute(self):
        sumn = self.m1+self.m2+self.m3
        print("Sum = " , sumn)
        print("Average = ", sumn/3)

arr=[]
n = int(input("Enter number of sudents"))
for i in range (0,n):
    a=input("Enter name: ")
    b=int(input("Enter Mark 1: "))
    c=int(input("Enter Mark 2: "))
    d=int(input("Enter Mark 3: "))
    arr.append(Student(a,b,c,d))

for i in range(0,n):
        print(arr[i].name)
        arr[i].compute()
