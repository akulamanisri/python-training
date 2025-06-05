#function
def add_contact(contacts):
    name = input("Enter Contact Name :")
    mobile = int(input("Enter mobile number :"))
    contacts[name] = mobile
    file=open("./phnum.txt","a")
    file.write(f"{name}:{mobile}\n")
    file.close()
def view_contacts(contacts):
    print("\n")
    #for i in contacts:
        #print(f"{i}:{contacts[i]}")
    file=open("./phnum.txt","r")
    contacts=file.readlines()
    for item in contacts:
        name,mobile=item.split(":")
        print(f"name:{name} mobile:{mobile}")
    file.close()
def delete_contact(contacts):
    name_to_delete = input("Enter contact name to delete :")
    del contacts[name_to_delete]
    print("deleted contact " , name_to_delete)
def find_contact(contacts):
    name = input("Enter name to search : ").lower()
    found = False
    file=open("./phnum.txt","r")
    for line in file:
        if name in line.lower():
            name, phone= line.split(":")
            print(f"Name: {name}, Phone: {phone}")
            found = True
            break
    if not found:
        print("Contact not found.")
    file.close()
    #for key in contacts:
        #if query in key:
            #print(f"{key} => {contacts[key]}")
            #found = True
    #if not found:
        #print("Query not Found!!!")


def edit_contact(contacts):
    name_to_edit = input("Enter contact name to edit :")
    number = int(input("Enter new number: "))
    contacts[name_to_edit] = number
    print("Edited contact : " , name_to_edit)
    