try:
    n=int(input())
    print(f"number is {n}")
except ValueError:
    print("value error occured")
finally:
    print("bye")