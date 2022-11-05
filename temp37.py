def function1(num1,num2,num3):
    if num1==num2:
        x1=num1
    else:
        while True:
            if num1>num2:
                num1=num1%num2
                if num1==0:
                    x1=num2
                    break
            if num2>num1:
                num2=num2%num1
                if num2==0:
                    x1=num1
                    break
    if x1!=num3:
        while True:
            if x1>num3:
                x1=x1%num3
                if x1==0:
                    return num3
            if num3>x1:
                num3=num3%x1
                if num3==0:
                    return x1
    return x1

def function2():
    x1=[]
    while True: 
        num1=input().split()
        if num1==['-1']:
            break
        x1.append(function1(int(num1[0]),int(num1[1]),int(num1[2])))
    for i in x1:
        print(i)

function2()