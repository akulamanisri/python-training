T=int(input())
for i in range(T):
    W,X,Y,Z=list(map(int,input().split()))
    per_mon=X*Z
    ded_mon=Y*Z
    deduced=per_mon-ded_mon
    print(W+deduced)
    