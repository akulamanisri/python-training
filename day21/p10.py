T = int(input())  
for i in range(T):
    X = int(input())  
    remainder = X % 10
    if remainder == 0:
        rounded_cost = X
    elif remainder <= 4:
        rounded_cost = X - remainder
    else:
        rounded_cost = X + (10 - remainder)

    change = 100 - rounded_cost
    print(change)
