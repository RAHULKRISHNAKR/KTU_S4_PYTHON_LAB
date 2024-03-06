number = int(input("Enter Number: "))
limit = int(input("Enter upto which number table is to be formed: "))

for i in range(1,limit+1):
    print(number," X ",i," = ", number*i)