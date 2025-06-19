T = int(input())  
for _ in range(T):
    n = int(input())  
    party_days = list(map(int, input().split()))
    unique_days = set(party_days)
    print(len(unique_days))