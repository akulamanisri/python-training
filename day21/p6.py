T = int(input())
for i in range(T):
    N = int(input())
    freq = {}
    for i in range(N):
        doll = int(input())
        if doll in freq:
            freq[doll] += 1
        else:
            freq[doll] = 1
    for i in freq:
        if freq[i] % 2 != 0:
            print(i)
            break
