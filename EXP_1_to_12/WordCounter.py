def counter(string):
    count=1
    string.split()
    for i in range(0,len(string)):
        if(string[i]==" "):
            count += 1
    return count

string = input("Enter sentence: ")
print("word count: ",counter(string))