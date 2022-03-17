l = []
# end = -1


def parent(ind):
    return (ind - 1) // 2


def right_child(ind):
    return (ind * 2) + 2


def left_child(ind):
    return (ind * 2) + 1


def display1(l,root1,space):
        if(root1>=len(l)):
             return 0 
        space=space+2
        if(right_child(root1)<len(l)):
            display1(l,right_child(root1),space)
        
        for i  in range(space):
            print(" ",end=" ")
        print(l[root1])
        if(left_child(root1)<len(l)):
            display1(l,left_child(root1),space)

        return 1

while (1):
    option = int(input("\n1.insert \n2.delete\n3.search\n4.display\n5.exit\nEnter your choice "))
    if (option == 1):
        val = int(input("Enter a value to insert"))
        l.append(val)
        curr = len(l)-1
        while (curr > 0):
            if (l[parent(curr)] < l[curr]):
                l[parent(curr)], l[curr] = l[curr], l[parent(curr)]
                curr=parent(curr)
            else:
                break
    elif(option==2):
        val=int(input("Enter a value to delete"))

        ind=-1
        i=0
        while i < len(l) :
            if(l[i]==val):
                end_val = l.pop()
                if(i==len(l)):
                    break
                l[i]=end_val
                while(i<len(l) and right_child(i)<len(l) and (end_val<l[left_child(i)] or end_val<l[right_child(i)])):
                    print(left_child(i),"  ",right_child(i))
                    if(l[left_child(i)] > l[right_child(i)]):
                        l[i],l[left_child(i)]=l[left_child(i)],l[i]
                        i=left_child(i)
                    else:
                        l[i], l[right_child(i)] = l[right_child(i)], l[i]
                        i = right_child(i)
                    print(l)
                if(i<len(l) and left_child(i)<len(l) and l[left_child(i)]>l[i]):
                    l[i],l[left_child(i)]=l[left_child(i)],l[i]
                break
            else:
                i+=1
            #     continue
            # break

    elif(option==3):
        val=int(input("Enter a value to search"))
        flag=True
        for i in l:
            if(i==val):
                print("Value found")
                flag=False
                break
        if(flag):
            print("not found")

        

    elif (option == 4):
        print(l)
        display1(l,0,0)
