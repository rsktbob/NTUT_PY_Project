x1 = int(input())
x2 = int(input())
x3 = int(input())

def function1(x1):
    t1 = 1
    if x1>=11 and x1<= 15:
        t1 = 0.95
    elif x1>=16 and x1<=20:
        t1 = 0.9
    elif x1>=21:
        t1 = 0.8
    k1 = x1*30*t1
    return k1

def function2(x2):
    t1 = 1
    if x2>=11 and x2<= 15:
        t1 = 0.9
    elif x2>=16 and x2<=20:
        t1 = 0.85
    elif x2>=21:
        t1 = 0.75
    k1 = x2*70*t1
    return k1

def function3(x3):
    t1 = 1
    if x3>=11 and x3<= 15:
        t1 = 0.85
    elif x3>=16:
        t1 = 0.8
    k1 = x3*40*t1
    return k1


if x1+x2+x3>=30:
    print(int((function1(x1) + function2(x2) + function3(x3))*0.87))
else:
    print(int((function1(x1) + function2(x2) + function3(x3))))