COUNT=10
class node:
	def __init__(self,key):
		self.data=key
		self.left=self.right=None
def insert(temp,num):
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
		if temp.left and temp.right :
			tempcell=findmin(temp.right)
			temp.data=tempcell.data
			temp.right=delete(temp.right, tempcell.data)
		elif(temp.right == None):
			temp=temp.left
		elif(temp.left == None):
			temp=temp.right
	return temp
def findmin(temp):
	while temp.left is not None:
		temp=temp.left
	return temp
def print2d(temp,space):
	if temp is None:
		return
	space += COUNT
	print2d(temp.right,space)
	print("\n")
	for i in range(COUNT,space):
		print(" ",end='')
	print("|"+str(temp.data)+"|<")
	print('\n')
	print2d(temp.left,space)
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
		print2d(root,0)