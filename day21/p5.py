T = int(input())

for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    min_value = min(A)
    ans = 0
    for x in A:
        if x > min_value:
            ans += 1
    print(ans)