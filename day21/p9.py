T = int(input()) 

for i in range(T):
    N = int(input())  
    A = list(map(int, input().split()))  
    freq = {}  

    for num in A:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    max_freq = 0
    for count in freq.values():
        if count > max_freq:
            max_freq = count
    max_count = 0
    for count in freq.values():
        if count == max_freq:
            max_count += 1
    if max_count == 1:
        print("YES")
    else:
        print("NO")
