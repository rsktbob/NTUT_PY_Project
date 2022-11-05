def function1(num1,num2=0,num3=1):
        if num1==1:
            return num3
        return function1(num1-1,num3,num3+num2)


def function2():
    x1=[]
    while True: 
        num1=int(input())
        if num1==-1:
            break
        x1.append(function1(num1))
    for i in x1:
        print(i)

function2()