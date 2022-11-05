def function1(num1):
    num2=''
    for i in num1:
        if i.isalpha()==True:
            num2=num2+i
    return num2

def function2(num1):
    num2=''
    for i in num1:
        if i.isupper()==True:
            num2=num2+i.lower()
        elif i.islower()==True:
            num2=num2+i.upper()
    return num2

def function3():
    num1=input().split()
    num1[0]=function1(num1[0])
    num1[0]=function2(num1[0])
    x1=len(num1[0])%int(num1[1])
    x2=[]
    x3=[]
    for i in range(0,len(num1[0])-x1,int(num1[1])):
        x2.append(num1[0][i:i+int(num1[1])])
    if x1!=0:
        x2.append(num1[0][len(num1[0])-x1::])
    for i in range(len(x2)-1,-1,-1):
        x3.append(x2[i])
    if len(num1[0])<int(num1[1]):
        print(num1[0])
        return
    x3='/'.join(x3)
    print(x3)

function3()
        
    

          
           