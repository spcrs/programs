

COUNT = 10


class node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def insert(temp, num):
    if temp is None:
        return node(num)
    elif(num > temp.data):
        temp.right = insert(temp.right, num)
    elif(num < temp.data):
        temp.left = insert(temp.left, num)
    else:
        print("Repeating is not allowed")
    return temp


def delete(temp, num):
    if temp is None:
        return
    elif(num < temp.data):
        temp.left = delete(temp.left, num)
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


def findmin(self, temp):
    while temp.left :
        temp = temp.left
    return temp


def print2d(temp,space):
	if temp is None:
		return
	space += COUNT
	print2d(temp.right,space)
	print("\n")
	for i in range(COUNT,space):
		print(" ",end='');
    print()


def inorder(root):
    if(root!=None):
        inorder(root.left)
        print(root.data)
        inorder(root.right)
root = None
ch = 5
while (ch != 4):
    ch=int(input("1.Insert\n2.Delete\n3.Print\n4.Exit\nChoose::"))
    if ch == 1:
        num=int(input("Enter the Number"))
        root=insert(root,num)
    elif ch == 2:
        num=int(input("Enter the Number"))
        root=delete(root,num)
    elif ch == 3:
        inorder(root)
    else:
        break



#print("|"+str(temp.data)+"|<")
	#print('\n')
	