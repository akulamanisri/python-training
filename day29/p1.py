arr=[0,2]
missing_number = arr[0]
list=range(0,len(arr)+1)

for i in range(1,len(arr)): # O(n)
    missing_number = missing_number ^ arr[i]

for i in list: #O(n)
    missing_number = missing_number ^ i

#O(n + n) => O(2n) => O(n) O(1) TC , SC => O(n) O(1)

print(missing_number)

