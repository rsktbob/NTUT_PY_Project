# -*- coding: utf-8 -*-
def function1(article):
    oddnum1="~!@#$%^&*<>_+="
    x1="1234567890"
    num1=0
    num2=0
    for i in range(len(article)-1):
        if article[i].islower()==True:
            num1=num1+1
        if article[i].isupper()==True:
            num1=num1+2
        if article[i] in oddnum1:
            num1=num1+5
        if article[i] in x1:
            num1=num1+3
            if article[i+1] not in x1:
                num2=num2+1                  
    if num2>=5:
        num1=num1+10
    return article,num1

def function2():
    x1={}
    x2=[]
    x3=[]
    while True:
        article=input()+" "
        if article=="-1 ":
            break
        num1,num2=function1(article)
        x1[num1]=num2
        x2.append(num2)
        x3.append(num1)
    x2.sort()
    for i in x3:
        if x1[i]==x2[len(x2)-1]:
            print(f'{i}{str(x2[len(x2)-1])}')
            break
    for i in x3: 
        if x1[i]==x2[0]:
            print(f'{i}{str(x2[0])}')
function2()
        
    
    