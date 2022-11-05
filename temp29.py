def function1():
    num1=input()
    num2=0
    num3=0
    t1=len(num1)
    t2=0
    k1=[]
    x1=[[1 for i in range(9)]for k in range(t1)]
    x2=0
    for i in range(t1):
        for k in range(9):
            if i!=0 and k!=0:
                x1[i][k]=x1[i-1][k]+x1[i][k-1]
            if i<=len(num1)-2:
                num2=num2+x1[i][k]
    for i in num1:
        k1.append(i)
    for i in range(t1):
        x3=int(k1[i])
        t1=t1-1
        if x3<=t2:
            x2=num2+num3
            return x2
        for k in range(t2,x3-1):
                num3=num3+x1[t1][8-k]
        t2=int(num1[i])-1
    x2=num2+num3+1
    return x2
    
print(function1())
 

        
