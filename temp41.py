def function1(num1):
    num2=''
    for i in range(len(num1)):
        if num1[i]=='[' and num1[i+1].isalpha()==True:
            num2=num2+"('"
        elif num1[i]=='[' and num1[i+1].isalpha()==False:
            num2=num2+'('
        elif num1[i]==']' and num1[i-1].isalpha()==True:
            num2=num2+"')"
        elif num1[i]==']' and num1[i-1].isalpha()==False:
            num2=num2+')'
        elif num1[i].isdigit()==True and num1[i-1].isalpha()==True and i!=0:
            num2=num2+f"'+{num1[i]}*"
        elif num1[i].isdigit()==True:
            num2=num2+f'+{num1[i]}*'
        else:
            num2=num2+num1[i]
    if num2[0].isalpha()==True:
        num2="'"+num2
    if num2[len(num2)-1].isalpha()==True:
        num2=num2+"'"
        i=len(num2)-2
        while True:
            if num2[i].isalpha()!=True:
               num2=num2[0:i+1]+"+'"+num2[i+1:]
               break
            i=i-1
    return eval(num2)
        
num1=input()
print(function1(num1))


    
        
        
        
    
