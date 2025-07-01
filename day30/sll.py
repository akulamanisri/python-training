class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
                
L=single()
n1=Node(10)
L.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
L.display()