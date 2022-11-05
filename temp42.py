def function1(n,count,result=1):
    if n==0:
        return result
    else:
        return function1(n-1,n-1,result+count)

num1=int(input())
print(function1(num1,num1))