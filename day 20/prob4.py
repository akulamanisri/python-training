n=int(input())
name_list=[]
for i in range(n):
    b=input()
    name_list.append(b)
search=input()
searched=[]
for x in name_list:
    if search.lower() in x.lower():
        searched.append(x)
print(searched)