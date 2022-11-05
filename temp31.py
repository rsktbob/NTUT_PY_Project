def function1():
    num1=input().split()
    num2=[int(num1[i])for i in range(0,6,2)]
    num3=[int(num1[i])for i in range(1,6,2)]
    x1=[int(num1[i])for i in range(0,6,2)]
    x1.sort()
    x2=num3[num2.index(x1[2])]
    t1=num3[num2.index(x1[0])]
    t2=num3[num2.index(x1[1])]
    k=0
    while True:
        x3=x1[2]*k+x2
        if x3%x1[0]==t1 and x3%x1[1]==t2:
            return x3
        k=k+1

print(function1())
    