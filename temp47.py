def function1(num1):
    x1=[]
    i=0
    while i<int(str((len(num1)-1))*(len(num1)))+1:
        x2=1
        for k in range(len(str(i))):
            if int(str(i)[k])>=len(num1):
                x2=0
                break
        if x2!=0:
            x1.append(i)
        i=i+1
    return x1

def function2(x1):
    for i in function1(x1):
        x2=[]
        for k in str(i):
            x2.append(int(k))
        x3=len(set(x2))
        if x3==len(x1):
            for t in x2:
                print(str(x1[t]),end='')
            print()
        elif x3==len(x1)-1 and len(str(i))==len(x1)-1:
            print(str(x1[0]),end='')
            for t in x2:
                print(str(x1[t]),end='')
            print()
        
x1=[1,2,3,4]     
function2(x1)    
       
        
        
