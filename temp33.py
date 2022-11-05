def function1():
    num1=input().split()
    num2=input().split()
    num3=[]
    x1={}
    for i in range(len(num1)):
        x1[int(num2[i])]=num1[i]
        num3.append(int(num2[i]))
    num3.sort()
    for i in num3:
        print(x1[i],end='')

function1()