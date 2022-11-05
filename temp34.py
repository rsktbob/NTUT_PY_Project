def function1(num1):
    num2=0
    for i in range(8):
        num2=num2+int(num1[i])*2**(7-i)
    return num2

def function2(num1):
    num2=''
    num3=0
    for i in range(4):
        if num1-num3>=2**(3-i):
            num2=num2+'1'
            num3=num3+2**(3-i)
        else:
            num2=num2+'0'
    return num2

def function3(num1,num2=0):
    if num1==0 or num1==1:
        return num2
    if num1%2==0:
        return function3(num1/2,num2+1)
    if num1%2==1:
        return function3((num1+1)/2,num2+1)
    
def function4():
    x1=[]
    while True:
        num1=input()
        if num1=='-1':
            break
        num1=function1(num1)
        num1=function3(num1)
        x1.append(function2(num1))
    for i in x1:
        print(i)
        
function4()        