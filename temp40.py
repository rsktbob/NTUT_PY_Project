def function1(num1,num2):
    x1=[]
    x3=0
    x4=0
    for i in range(num1):
        x2=input().split()
        if len(x2)!=num2:
            return
        x1.append(x2)
    for i in range(num1):
        for k in range(num2):
            x3=0
            for r in range(num1):
                for t in range(num2):
                    x3=x3+int(x1[r][t])*(abs(r-i)+abs(t-k))*100
            if x3<x4 or x4==0:
                x4=x3
                t1=i+1
                t2=k+1

    return x4,t1,t2

def function2():
    x1=int(input())
    x2=input().split()
    x3=[]
    for i in range(x1):
        num1=int(x2[0])
        num2=int(x2[1])
        x3.append(function1(num1,num2))
    for i in range(x1):
        print(x3[i][1],x3[i][2])
        print(x3[i][0])
    
function2()    
                 
                
                
                
            