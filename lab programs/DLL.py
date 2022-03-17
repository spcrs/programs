class Node:
	def __init__(self,val):
		self.val=val
		self.right=None
		self.left=None
class DLL:
	def __init__(self):
		self.head=None
	def insert(self,val):
		if(self.head==None):
			self.head=Node(val)
			self.head.right=self.head
			self.head.left=self.head
			return
		newNode=Node(val)
		tail=self.head.left

		tail.right=newNode
		newNode.left=tail
		newNode.right=self.head
		
		self.head.left=newNode

	def delete(self,val):
		if(self.head==None):
			print("underflow error")
			return
	
		if(self.head.val==val):
			if(self.head.right==self.head):
				self.head=None
				return
			tail=self.head.left
			tail.right=self.head.right
	
			self.head=self.head.right	
			self.head.left=tail
			return
		temp=self.head.right
		while(temp.val!=val and temp!=self.head):
			temp=temp.right
		if(temp==self.head):
			print("search value not found")
			return
		
		le=temp.left
		ri=temp.right
		
		le.right=ri
		ri.left=le
		
			
			
	def display(self):
		temp=self.head
		if(temp!=None):
			print("dfhj",temp.val)
		temp=temp.right
		while(temp!=self.head):
			print(temp.val)
			temp=temp.right


doubly=DLL()

n=int(input("Enter no of values"))

for i in range(n):
	val=int(input("enter a value"))
	doubly.insert(val)

	doubly.display()

for i in range(n-2):
	val=int(input("Enter a value to delete"))
	doubly.delete(val)
		
	doubly.display()