class Node:                                                                     
     def __init__(self, val):
         self.val = val                                                       
         self.prev = None
         self.next = None
head = tail = None
def append_node():                                                           
    val = int(input("Enter Number to be inserted :"))
    global head, tail
    node = Node(val)
    if head is None:                                                            
        head = tail = node
    else:                                                                       
        tail.next = node
        node.prev = tail
        tail = node
def front_node():                                                         
    val = int(input("Enter Number to be inserted :"))
    global head, tail
    node = Node(val)
    if head is None:                                                            
        head = tail = node
    else:
        node.next = head
        head.prev = node
        head = node
def remove_front():
    global head, tail
    if(head is None):
        print("List is Empty...!")
    elif(head is tail):
        print(head.val," is Deleted..!")
        head = tail = None
    else:
        print(head.val, " is Deleted..!")
        temp = head
        head = head.next
        head.prev = None
def remove_end():
    global head, tail
    if(head is None):
        print("List is Empty...!")
    elif(head is tail):
        print(tail.val, " is Deleted..!")
    else:
        print(tail.val, " is Deleted...!")
        tail = tail.prev
        tail.next = None
def remove_node():
    val = int(input("Enter the Number to Delete :"))
    global head, tail
    current_node = head
    previous_node = None
    while(current_node is not None):
        if (current_node.val == val):
            if(head is tail):
                head=tail=None
            elif (previous_node is None):
                current_node.next.prev = None
                head = current_node.next
            elif(current_node is tail):
                previous_node.next=None
                tail=previous_node
            else:
                current_node.next.prev = current_node.prev
                previous_node.next = current_node.next
        previous_node = current_node
        current_node = current_node.next
def print_list():                                                               
    global head, tail
    if(head is None):
        print("List is Empty...!")
    else:
        print("Double linked list")
        current_node = head
        while(current_node is not tail):
            print (current_node.val,"<==> ",end="")
            current_node = current_node.next
        print (tail.val, end="\n")
def reverse_linked_list():
    global head, tail
    if(head is None):
        print("List is Empty...!")
    else:
        print("Double linked list reverse order")
        current_node = tail
        while(current_node is not head):
            print (current_node.val, "<==> ", end=" ")
            current_node = current_node.prev
        print(head.val, end="\n")
def option(ch):
    switcher = {
        1: front_node,
        2: append_node,
        3: remove_front,
        4: remove_node,
        5: remove_end,
        6: print_list,
        7: reverse_linked_list,
    }
    func=switcher.get(ch, lambda: "Invalid Option ") 
    return func()                                                                            
if __name__ == "__main__":  
    ch = 1
    while(ch != 8):
        print("1.Inser at Front\n2.Insert at End\n3.Delete the Front\n4.Delete the Number\n5.Delete at End\n6.Display\n7.Display in Reverse\n8.Exit")
        ch = int(input("your option:"))
        option(ch)