def function1():
    num1=input().split()
    num2=[]
    num3=[]
    for i in num1:
        if int(i)%2==1:
            num2.append(int(i))
        else:
            num3.append(int(i))
    num2.sort()
    num3.sort(reverse=True)
    num2.extend(num3)
    return num2
            
print(function1())