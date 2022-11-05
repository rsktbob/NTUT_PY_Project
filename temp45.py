from itertools import combinations

def function1():
    num1=input().split()
    num2=list(combinations(num1[0],int(num1[1])))
    x1=[]
    for i in num2:
        x1.append(''.join(i))
    x1.sort()
    x1=' '.join(x1)
    print(x1)
        
function1()    
    
    