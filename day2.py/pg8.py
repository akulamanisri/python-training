my_list=[2,3,5,7,9,11,14]
x=int(input())
for i in range(0,len(my_list)):
    if x== my_list[i]:
        print("found")
        break
    else:
        print("not found")
        break