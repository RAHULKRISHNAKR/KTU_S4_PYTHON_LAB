def rm(arr, digit):
  newarr = []
  for num in arr:
    strnum = str(num)
    newnum = strnum.replace(str(digit), "")
    if newnum:
      newarr.append(int(newnum))

  return newarr

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
digit = int(input("Enter the digit to remove: "))

newarr = rm(arr, digit)

print("Original array:", arr)
print("Modified array:", newarr)
