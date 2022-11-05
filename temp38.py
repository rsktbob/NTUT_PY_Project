def function1(num1,num2=0,num3=1):
        if num1==1:
            return num3
        return function1(num1-1,num3,num3*2+num2*3)

def function2(): 
    num1=float(input())
    if num1<2 or num1%1!=0:
        print("Error")
        return
    print(function1(num1,num2=0,num3=1))
    return

function2()