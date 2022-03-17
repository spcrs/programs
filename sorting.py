
# #2)sorting
n=int(input("enter the number of values"))
arr=[]
sum=0
for i in range(n):
    arr+=[int(input("Enter the values"))]
print(arr)


for i in range(n):
    for j in range(i+1,n):
        if(arr[i]>arr[j]):
            arr[i],arr[j]=arr[j],arr[i]
print(arr)

