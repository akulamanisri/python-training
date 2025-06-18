list=input().split(" ")
print(list)
search=input()
searched=[]
for x in list:
    if search.lower() in x.lower():
        searched.append(x)
print(searched)