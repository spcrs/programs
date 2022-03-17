class LinkedList:
     def __init__(self):
         self.head=None
         self.tail=None
     def addAtHead(self,val):
         new=Node(val);
         if(self.head==None):
             self.head=new
             self.tail=new
         else:
             new.next=self.head
             self.head.prev=new
             self.head=new
     def addAtTail(self,val):
         if(self.head==None):
             self.addAtHead(val)
         else:
             new=Node(val)
             self.tail.next=new
             new.prev=self.tail
             tail=new
     def addBeforeValue(self,val,b):
         if(self.head==None):
             print("Linked list is empty")
         elif(self.head.data==b):
             self.addAtHead(val)
         else:
             new=Node(val);
             prev=self.head;
             temp=self.head.next;
             while(temp!=None):
                 if(temp.data==b):
                     prev.next=new
                     new.prev=prev
                     new.next=temp
                     temp.prev=new
                     return
                 prev=temp
                 temp=temp.next
             print("No such value found")
     def display(self):
         temp=self.head
         print("\n")
         while(temp!=None):
             print(temp.data," -> ",end=" ")
             temp=temp.next
         print("\n")
     def delete(self,val):
         if(self.head==None):
             print("List is empty")
         if(self.head.data==val):
             self.head=self.head.next
             self.head.prev=None
         else:
             prev=self.head
             temp=self.head.next
             while(temp!=None):
                 if(temp.data==val):
                     prev.next=temp.next
                     temp.next.prev=prev
                     return
                 prev=temp
                 temp=temp.next
             print("No such value found")
class Node:
     def __init__(self,val):
         self.data=val
         self.next=None
         self.prev=None

li=LinkedList()
while(1):
     n=int(input("Enter your choice\n1.insert at beginning   2.insert at end\n3.inser before value    4.display\n5.delete   6.exit"))
     if(n==1):
         va=int(input("Enter the value to insert"))
         li.addAtHead(va)
     elif(n==2):
         va = int(input("Enter the value to insert"))
         li.addAtTail(va)
     elif(n==3):
         va = int(input("Enter the value to insert"))
         b = int(input("Enter the value before you want to insert"))
         li.addBeforeValue(va,b)
     elif(n==4):
         li.display()
     elif(n==5):
         va=int(input("Enter the value to delete"))
         li.delete(va)
     else:
         break;
print("process completed")


