def add_student(gradebook):
    name=input("enter name:")
    mark=input("emter marks:")
    mark_list=list(map(int,mark.split()))
    gradebook[name]=mark_list
    
def view_student(gradebook):
    if not gradebook:
        print("There is no students in gradebook\nAdd students")
        return
    print("students in gradebook")
    for name,mark in gradebook.items():
        avg=sum(mark) / len(mark)
        print(f"{name}-mark:{mark} avg:{avg}")
def delete_student(gradebook):
    name_to_delete=input("enter the student to delete:")
    del gradebook[name_to_delete]
    print("delete student:",name_to_delete)
def edit_student(gradebook):
    name=input("enter the student to edit:")
    if name in gradebook:
     mark=input("enter the marks")
     mark_list=list(map(int ,mark.split()))
     gradebook[name]=mark_list
     print("edit student",name)
    else:
        print("student not  found")
def search_student(gradebook):
    student_to_search=input("enter student to search").lower()
    found=False
    for name,mark in gradebook.items():
        if student_to_search in name.lower():
            avg:sum(mark)/len(mark)
            print(f"{name}-mark:{mark} avg:{avg}")
            found=True
    if not found:
        print("student not found")

