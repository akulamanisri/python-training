class human:
    hands=2
    legs=2
    def eat(self):
        print("I am eating")
x=human()
print(x.hands)
x.eat()
class female(human):
    gender="female"
    def greet(self):
        print("hi guys")
y=female()
print(y.gender)
y.greet()