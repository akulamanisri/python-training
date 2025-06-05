class Student():
    name=""
    rollno=0
    def display_info(self):
        print(f"{self.name} has {self.rollno}")
student1=Student()
student1.name="ram"
student1.rollno=98
print(student1.name)
student1.display_info()