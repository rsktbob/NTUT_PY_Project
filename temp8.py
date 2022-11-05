def function1(x1=[],x2=1):
    x1 = []
    x2 = int(input())
    for i in range(x2):
       x1.append(int(input()))
    return x1

def function2(t1,t2,x1,x2):
    for i in range(len(t1)):
        for k in range(len(t2)):
            if t1[i] == t2[k]:
                print(f"{x1} and {x2} on confict is {t2[k]}")


x1 = input()
t1 = function1()
x2 = input()
t2 = function1()
x3 = input()
t3 = function1()
function2(t1,t2,x1,x2)
function2(t2,t3,x2,x3)
function2(t1,t3,x1,x3)

 
