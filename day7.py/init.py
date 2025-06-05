class student:
    name=""
    roll=0
    def __init__(self,x,y):
        self.name=x
        self.roll=y
    def display_info(self):
        print(f"{self.name}has {self.roll}")
    def __str__(self):
        return "{self.name}"
student1=student("ram",98)
print(student1.name)