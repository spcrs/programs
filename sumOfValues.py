#1)sum of values
# n=int(input("enter the number of values"))
# arr=[]
# sum=0
# for i in range(n):
#     arr+=[int(input("Enter the values"))]
# print(arr)
#
#
# for i in arr:
#     sum+=i
# print("The sum is ",sum)













#
# # 3)fibbonacci series
# f=0
# s=1
# t=1
# n=int(input("Enter no of values"))
# i=2
# print(f,"\n",s)
# while(i<n):
#     t=f+s
#     print(t)
#     f=s
#     s=t
#     i+=1



# # 5)greatest of three numbers
# a=int(input("Enter values"))
# b=int(input("Enter values"))
# c=int(input("Enter values"))
# if(a>b):
#     if(a>c):
#         print("The biggest value is ",a)
#     else:
#         print("The biggst value is ",c)
# elif(b>c):
#     print("The biggest value is ",b)
# else:
#     print("The biggest value is ",c)




#6)palindrome or not
# rev=0
# n=int(input("Enter the value to check palindrome"))
# n1=n
# while(n1>0):
#     rem=n1%10
#     rev=rev*10+rem
#     n1=n1//10
# print(rev)
# if(rev==n):
#     print("Given value is palindrome")
# else:
#     print("Given value is not palindrome")


# 7)LinkedList
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def addAtHead(self,val):
#         new=Node(val);
#         if(self.head==None):
#             self.head=new
#             self.tail=new
#         else:
#             new.next=self.head
#             self.head.prev=new
#             self.head=new
#     def addAtTail(self,val):
#         if(self.head==None):
#             self.addAtHead(val)
#         else:
#             new=Node(val)
#             self.tail.next=new
#             new.prev=self.tail
#             tail=new
#     def addBeforeValue(self,val,b):
#         if(self.head==None):
#             print("Linked list is empty")
#         elif(self.head.data==b):
#             self.addAtHead(val)
#         else:
#             new=Node(val);
#             prev=self.head;
#             temp=self.head.next;
#             while(temp!=None):
#                 if(temp.data==b):
#                     prev.next=new
#                     new.prev=prev
#                     new.next=temp
#                     temp.prev=new
#                     return
#                 prev=temp
#                 temp=temp.next
#             print("No such value found")
#     def display(self):
#         temp=self.head
#         print("\n")
#         while(temp!=None):
#             print(temp.data," -> ",end=" ")
#             temp=temp.next
#         print("\n")
#     def delete(self,val):
#         if(self.head==None):
#             print("List is empty")
#         if(self.head.data==val):
#             self.head=self.head.next
#             self.head.prev=None
#         else:
#             prev=self.head
#             temp=self.head.next
#             while(temp!=None):
#                 if(temp.data==val):
#                     prev.next=temp.next
#                     temp.next.prev=prev
#                     return
#                 prev=temp
#                 temp=temp.next
#             print("No such value found")
# class Node:
#     def __init__(self,val):
#         self.data=val
#         self.next=None
#         self.prev=None
#
# li=LinkedList();
# while(1):
#     n=int(input("Enter your choice\n1.insert at beginning   2.insert at end\n3.inser before value    4.display\n5.delete   6.exit"))
#     if(n==1):
#         va=int(input("Enter the value to insert"))
#         li.addAtHead(va)
#     elif(n==2):
#         va = int(input("Enter the value to insert"))
#         li.addAtTail(va)
#     elif(n==3):
#         va = int(input("Enter the value to insert"))
#         b = int(input("Enter the value before you want to insert"))
#         li.addBeforeValue(va,b)
#     elif(n==4):
#         li.display()
#     elif(n==5):
#         va=int(input("Enter the value to delete"))
#         li.delete(va)
#     else:
#         break;
# print("process completed")



#8)stack implementations
# class Stack:
#     def __init__(self):
#         self.top=-1
#         self.limit=10
#         self.stack = [0,0,0,0,0,0,0,0,0,0,0,0]
#     def push(self,val):
#         if(self.top==self.limit):
#             print("stack is full")
#         else:
#             self.top+=1
#             self.stack[self.top]=val
#     def pop(self):
#         if(self.top==-1):
#             print("stack is empty")
#         else:
#             self.top-=1
#     def display(self):
#         print("The values are")
#         for i in range(self.top+1):
#             print(self.stack[i]," ",end=" ")
#     def peek(self):
#         if(self.top==-1):
#             print("stack is empty")
#         else:
#             print("The element at top is ",self.stack[self.top])
#
#
# stack=Stack();
# while(1):
#     n=int(input("Enter your choice \n1.push\n2.pop\n3.peek\n4.display\n5.exit"))
#     if(n==1):
#         val=int(input("Enter the value to push"))
#         stack.push(val)
#     elif(n==2):
#         stack.pop()
#     elif(n==3):
#         stack.peek()
#     elif(n==4):
#         stack.display()
#     else:
#         break
#
#
#
# #8)Quick sort

# def partition(arr,l,h):
#     i=l-1
#     p=arr[h]
#     for j in range(l,h):
#         if(arr[j]<=p):
#             i+=1
#             arr[i],arr[j]=arr[j],arr[i]
#     arr[i+1],arr[h]=arr[h],arr[i+1]
#     return i+1
#
# def quickSort(arr,l,h):
#     if(len(arr)==1):
#         return
#     if(l<h):
#         pi=partition(arr,l,h)
#         quickSort(arr,l,pi-1)
#         quickSort(arr,pi+1,h)
#
#
# arr=[]
# n=int(input("Enter no of values"))
# for i in range(n):
#     val=int(input("Enter the value"))
#     arr.append(val)
# print(arr)
# quickSort(arr,0,n-1)
# print("After sorting ",arr)




size=int(input("Enter the size of stack"))
top=-1
a=["*"]*size
print(a)
#push
def push():
    global top,a,size
    if(top==size-1):
        print("stack is full")
        return
    top+=1
    val=int(input("Emnter a va;ie"))
    a[top]=val
def pop():
    global top,a
    if(top==-1):
        print("stack is empty")
        return
    top-=1
    print("The popped value is ",a[top+1])
def peek():
    global top,a
    if(top==-1):
        print("stack is empty")
        return
    print("The peek element",a[top])

def display():
    global top,a


    for i in range(top,-1,-1):
        print(a[i])
while(1):
    n=int(input("Enter your choice \n1.push\n2.pop\n3.peek\n4.display\n5.exit"))
    if(n==1):
        push()
    elif(n==2):
        pop()
    elif(n==3):
        peek()
    elif(n==4):
        display()
    else:
        break




COUNT=10
class node:
    def __init__(self,key):
	    self.data=key
	    self.left=self.right=None

    def insert(self,temp,num):
        if temp is None:
            return node(num)
        elif(num > temp.data):
            temp.right = insert(temp.right,num)
        elif(num < temp.data):
            temp.left = insert(temp.left,num)
        else:
            print("Repeating is not allowed")
        return temp

    def delete(temp,num):
        if temp is None:
            return
        elif(num < temp.data):
            temp.left=delete(temp.left,num)
        elif(num < temp.data):
            temp.right = delete(temp.right, num)
        else:
            if(temp.right == None):
                return temp.left
            elif(temp.left == None):
                return temp.right
            tempcell = findmin(temp.right)
            temp.data = tempcell.data
            temp.right = delete(temp.right, tempcell.data)
        return temp

    def findmin(self,temp):
        while temp.left is not None:
            temp=temp.left
        return temp


# def print2d(temp,space):
# 	if temp is None:
# 		return
# 	space += COUNT
# 	print2d(temp.right,space)
# 	print("\n")
# 	for i in range(COUNT,space):
# 		print(" ",end='')
# 	print("|"+str(temp.data)+"|<")
# 	print('\n')
# 	print2d(temp.left,space)


def inorder(root):
    if(root!=None):
        inorder(root.left)
        print(root.val)
        inorder(root.right)
root = None
ch = 5
while (ch != 4):
	ch=int(input("1.Insert\n2.Delete\n3.Print\n4.Exit\nChoose::"))
	if ch is 1:
		num=int(input("Enter the Number"))
		root=insert(root,num)
	elif ch is 2:
		num=int(input("Enter the Number"))
		root=delete(root,num)
    elif ch is 3:
        inorder(root)
    else:
        break

