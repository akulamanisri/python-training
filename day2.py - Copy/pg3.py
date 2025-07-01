import pg2 as m
number_1=int(input())
while True:
    op=input()
    if op=="=":
        print(number_1)
        break
    number_2=int(input())
    if op=='+':
        number_1=m.add(number_1,number_2)
    elif op=="-":
        number_1=m.sub(number_1,number_2)
    elif op=="*":
        number_1=m.mul(number_1,number_2)
    elif op=="/":
        number_1=m.div(number_1,number_2)
