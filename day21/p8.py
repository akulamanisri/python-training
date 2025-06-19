T = int(input())  
for i in range(T):
    N = int(input())  
    A = list(map(int, input().split())) 
    freq = {}
    for i in A:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    max_freq = 0
    for value in freq.values():
        if value > max_freq:
            max_freq = value
    print(N - max_freq)
