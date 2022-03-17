class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BST:
        
    def __init__(self):
        self.root=None
    
    def insert(self,root1,val):
        if(root1==None):
                return Node(val)
        elif(root1.val<val):
            root1.right=self.insert(root1.right,val)
        elif(root1.val>val):
            root1.left=self.insert(root1.left,val)
        return root1

    def display1(self,root1,space):
        if(root1==None):
            return
        space=space+2
        self.display1(root1.right,space)
        
        for i  in range(space):
            print(" ",end=" ")
        print(root1.val)
        self.display1(root1.left,space)

    def inorder(self,root1):
        if(root1==None):
            return
        self.inorder(root1.left)
        print(root1.val," ",end=" ")
        self.inorder(root1.right)

    def preorder(self,root1):
        if(root1==None):
            return
        print(root1.val," ",end=" ")
        self.preorder(root1.left)
        self.preorder(root1.right)

    def postorder(self,root1):
        if(root1==None):
            return
        self.postorder(root1.left)
        self.postorder(root1.right)
        print(root1.val," ",end=" ")
        

    def delete(self,root1,val):
    
        if(root1==None):
            return
        if(root1.val<val):
            root1.right=self.delete(root1.right,val)
        elif(root1.val>val):
            root1.left=self.delete(root1.left,val)
        else:
            if(root1.left==None):
                return root1.right
            elif(root1.right==None):
                return root1.left
            else:
                min=self.findMin(root1.right)
                root1.val=min
                root1.right=self.delete(root1.right,min)
        return root1

    def findMin(self,root1):
        while(root1.left!=None):
            root1=root1.left
        return root1.val
        
bst=BST()


n=int(input("Enter no of values"))
for i in range(n):
    val=int(input("Enter a value to insert"))
    bst.root=bst.insert(bst.root,val)
bst.display1(bst.root,0)


print("inorder ",bst.inorder(bst.root))
print("preorder ",bst.preorder(bst.root))
print("postorder ",bst.postorder(bst.root))

for i in range(n-3):
    val=int(input("Enter a value to delete"))
    bst.root=bst.delete(bst.root,val)
    bst.display1(bst.root,0)
