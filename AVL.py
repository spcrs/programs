COUNT = 5


class node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.height=1

def height(temp):
    if(temp==None):
        return 0
    return temp.height;

def getBalance(root):
    if(root==None):
        return 0
    return height(root.left)-height(root.right)

def max(a,b):
    if(a>b):
        return a
    else:
        return b

def leftRotation(temp):
    n=temp.right
    t=n.left

    n.left=temp
    temp.right=t

    temp.height = 1 + max(height(temp.left), height(temp.right))
    n.height=1+max(height(n.left),height(n.right))
    return n

def rightRotation(temp):
    n=temp.left
    t=n.right

    n.right=temp
    temp.left=t

    temp.height = 1 + max(height(temp.left), height(temp.right))
    n.height=1+max(height(n.left),height(n.right))

    return n



def insert(root1, num):
    if root1 is None:
        return node(num)
    elif (num > root1.data):
        root1.right = insert(root1.right, num)
    elif (num < root1.data):
        root1.left = insert(root1.left, num)
   # else:
    #    print("Repeating is not allowed")
     #   return None
    # print2d(root1, 1)
    root1.height= 1 + max(height(root1.left), height(root1.right))
    balance=getBalance(root1)
    if(balance<-1 and root1.right.data<num):
        return leftRotation(root1)
    if(balance>1 and root1.left.data>num):
        return rightRotation(root1)
    if(balance<-1 and root1.right.data>num):
        root1.right=rightRotation(root1.right)
        return leftRotation(root1)
    if(balance>1 and root1.left.data<num):
        root1.left=leftRotation(root1.left)
        return rightRotation(root1)
    return root1



def delete(root1, num):
    if root1 is None:
        return
    elif (num < root1.data):
        root1.left = delete(root1.left, num)
    elif (num > root1.data):
        root1.right = delete(root1.right, num)
    else:
        if (root1.right == None):
            return root1.left
        elif (root1.left == None):
            return root1.right
        temp = findmin(root1.right)
        root1.data = temp.data
        root1.right = delete(root1.right, temp.data)

    if root1==None:
        return root1
    root1.height= 1 + max(height(root1.left), height(root1.right))
    balance=getBalance(root1)

    if (balance < -1 and root1.right.data < num):
        return leftRotation(root1)
    if (balance > 1 and root1.left.data > num):
        return rightRotation(root1)
    if (balance < -1 and root1.right.data > num):
        root1.right = rightRotation(root1.right)
        return leftRotation(root1)
    if (balance > 1 and root1.left.data < num):
        root1.left = leftRotation(root1.left)
        return rightRotation(root1)
    return root1


def findmin(temp):
    while temp.left:
        temp = temp.left
    return temp


def print2d(temp, space):
    if temp is None:
        return
    space += COUNT
    print2d(temp.right, space)
    print("")
    for i in range(COUNT, space):
        print(" ", end='')
    print(temp.data,end=" ")
    print2d(temp.left,space)


def inorder(root1):
    if (root1 != None):
        inorder(root1.left)
        print(root1.data)
        inorder(root1.right)


root = None
ch = 5
while (ch != 4):
    ch = int(input("\n1.Insert\n2.Delete\n3.Print\n4.Exit\nChoose::"))
    if ch == 1:
        num = int(input("Enter the Number"))
        root = insert(root, num)
    elif ch == 2:
        num = int(input("Enter the Number"))
        root = delete(root, num)
    elif ch == 3:
        print("This is the tree")
        print2d(root,1)


# print("|"+str(temp.data)+"|<")
# print('\n')



# class Node:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
#     def insert(self,root,val):
#         if(root==None):
#            return None
#         if(root.val<val):
#             root.right=self.insert(root.right,val)
#         elif(root.val>val):
#             root.left=self.insert(root.left,val)
#         return root;
#
# n=int(input("Enter no of values to insert"))
# for i in range(n):
#     val = int(input("Enter a value"))
#     if(i==0):
#         root=Node(val)

#
#
#
# COUNT=10
# class node:
#     def __init__(self,key):
# 	    self.data=key
# 	    self.left=self.right=None
#
# def insert(temp,num):
#         if temp is None:
#             return node(num)
#         elif(num > temp.data):
#             temp.right = insert(temp.right,num)
#         elif(num < temp.data):
#             temp.left = insert(temp.left,num)
#         else:
#             print("Repeating is not allowed")
#         return temp
#
# def delete(temp,num):
#         if temp is None:
#             return
#         elif(num < temp.data):
#             temp.left=delete(temp.left,num)
#         elif(num < temp.data):
#             temp.right = delete(temp.right, num)
#         else:
#             if(temp.right == None):
#                 return temp.left
#             elif(temp.left == None):
#                 return temp.right
#             tempcell = findmin(temp.right)
#             temp.data = tempcell.data
#             temp.right = delete(temp.right, tempcell.data)
#         return temp
#
# def findmin(self,temp):
#         while temp.left is not None:
#             temp=temp.left
#         return temp
#
#
# def print2d(temp,space):
# 	if temp is None:
#         return
# 	space += COUNT
# 	print2d(temp.right,space)
# 	print("\n")
# 	for i in range(COUNT,space):
# 		print(" ",end='')
#     print(temp.data)
# 	# print("|"+str(temp.data)+"|<")
# 	# print('\n')
# 	print2d(temp.left,space)
#
#
# def inorder(root):
#     if(root!=None):
#         inorder(root.left)
#         print(root.val)
#         inorder(root.right)
# root = None
# ch = 5
# while (ch != 4):
#     ch=int(input("1.Insert\n2.Delete\n3.Print\n4.Exit\nChoose::"))
#     if ch == 1:
#         num=int(input("Enter the Number"))
#         root=insert(root,num)
#     elif ch == 2:
#         num=int(input("Enter the Number"))
#         root=delete(root,num)
#     elif ch == 3:
#         inorder(root)
#     else:
#         break
#
