t = int(input())

while t > 0:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    s=sum(a)
    new_list=[]
    for i in a:
        if i>y:
            new_list.append(i-y)
        else:
            new_list.append(0)
    s1=sum(new_list)
    s1+=x
    if s1<s:
        print("COUPON")
    else:
        print("NO COUPON")