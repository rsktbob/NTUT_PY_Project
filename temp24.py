def function1():
    x1 = input()
    card = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':0.5,'Q':0.5,'K':0.5}
    return card[x1]

def function2(x1,num1):
    if num1 == 0:
       return 0
    elif x1 == 'Y':
       return 1
    elif x1 == 'N':
       return 0
    
        
def function3(num1,num2,num3):
    if num2 == 0:
        return 0
    if num3 == 0:
        return 0
    elif num2<=8 or num2<num1:
        return 1
    else:
        return 0
            
def function4(num1,num2):
    if num1>10.5:
        num1=0
    if num2>10.5:
        num2=0
    return num1,num2
            
def function5(num1,num2):
    x1 ='Y'
    num3 = 1
    while True:
        num1,num2=function4(num1,num2)
        if function2(x1,num1) == 1:
            x1 = input()
        if function2(x1,num1) == 1 and function3(num1,num2,num3) == 1:
            num1 = num1+function1()
            num2 = num2+function1()
        elif function2(x1,num1) == 1 and function3(num1,num2,num3) == 0:
            num1 = num1+function1()
            num3 = 0
        elif function2(x1,num1) == 0 and function3(num1,num2,num3) == 1:
            num2 = num2+function1()
        elif function2(x1,num1) == 0 and function3(num1,num2,num3) == 0:
            return num1,num2
        
def function6():
    num1=function1()
    num2=function1()
    num1,num2=function5(num1,num2)
    num1=float('%.1f'%num1)
    num2=float('%.1f'%num2)
    print(f'{num1} vs. {num2}')
    if num1>num2:
        print("player wins")
    if num1==num2:
        print("It's a tie")
    if num1<num2:
        print("computer wins")

function6()    

 
            
            
            
        
        