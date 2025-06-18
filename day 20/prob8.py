def slug_generator(x:str):
    x=x.lower()
    x=list(x)
    result=""
    for i in range(0,len(x)):
        if x[i].isalnum():
            result+=x[i]
        elif x[i]==" ":
            result+="-"
        else:
            continue
    return result
title=input()
result=slug_generator(title)
print(result)