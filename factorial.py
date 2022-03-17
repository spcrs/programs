# #2)factorial
n=int(input("enter the value"))
ans=1
for i in range(1,n+1):
    ans*=i
print("Factorial of ",n," is ",ans)
