def function1():
    num1=input()
    x1=[]
    t1=[]
    for i in range(len(num1)):
        for k in range(len(num1)):
            x1.append(num1[i:k+1])
    x1=list(set(x1))
    x1.sort()
    for i in range(len(x1)):
        t2=x1[i][-1::-1]
        if x1[i]==t2:
            t1.append(t2)
    t1='#'.join(t1)
    t1=t1[1::]
    print(t1)
    
function1()