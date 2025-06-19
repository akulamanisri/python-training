T = int(input())

for i in range(T):
    
    N, X = map(int, input().split())

    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    
    total_cost = 0
    for i in range(N):
        if A[i] >= X:
            total_cost += B[i]

    print(total_cost)
