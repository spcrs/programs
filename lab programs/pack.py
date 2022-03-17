class Mathametics:
    def power(self,val,pow):
        ans=1
        for i in range(pow):
            ans*=val
        return ans

def sum(*vals):
    sum=0
    for i in vals:
        sum+=i
    return sum
  
val=10

def fun(a,b):
    return a+b