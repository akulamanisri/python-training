user_list=[]
n=int(input())
for i in range(n):
    user_dict={}
    user_dict["name"]=input()
    user_dict["id"]=int(input())
    user_list.append(user_dict)
print(user_list)