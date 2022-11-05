def function1(num1):
    for i in range(2,16):
        for k in range(1,16):
            for t in range(16):
                if i>k>t>=0:
                    x1=i*(i-1)*(i-2)/6
                    x2=k*(k-1)/2
                    num2=x1+x2+t
                    if num1==num2:
                        return str(i)+str(k)+str(t)
                else:
                    break
            
def function2():
    x1=[]
    num2=int(input())
    for i in range(num2): 
        num1=int(input())
        if num1==-1:
            break
        num2=function1(num1)
        if num2!=None:
            x1.append(int(num2))
    for i in x1:
        print(i)


function2()