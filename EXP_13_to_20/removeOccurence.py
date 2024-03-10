def rm(arr, d):
  newarr = []
  for num in arr:
    strn = str(num)
    if str(d) not in strn:
      newarr.append(num)
      continue

    first_occ = strn.find(str(d))
    modified_num = strn[:first_occ + 1] + strn[first_occ + 1:].replace(str(d), "")
    newarr.append(int(modified_num))
  return newarr

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
digit = int(input("Enter the digit to remove: "))

new_arr = rm(arr.copy(), digit)

print("Original array:", arr)
print("Modified array:", new_arr)
