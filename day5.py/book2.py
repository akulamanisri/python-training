import book as b 
gradebook={}

while True:
    print("\n\n choose your choice")
    print("1.Add students")
    print("2.view student")
    print("3.Delete contact")
    print("4.Edit contact")
    print("5.search student")
    print("6.exit")

    choice=input("enter your choice:")
    if choice=="1":
        b.add_student(gradebook)
    elif choice=="2":
        b.view_student(gradebook)
    elif choice=="3":
        b.delete_student(gradebook)
    elif choice=="4":
        b.edit_student(gradebook)
    elif choice=="5":
        b.search_student(gradebook)
    elif choice=="6":
        print("exit")
    else:
        print("INVALID CHOICE!! please enter valid choice")