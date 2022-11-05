from functools import reduce

def add(x1):
    x1 = x1+3
    return x1

def istnum(x1):
    if(x1 == 3):
        return True
    else:
        return x1%2 == 0

x1 = [i for i in range(6)]
x2 = list(map(lambda x:x+3,[1,2,3,4,5,6]))
print(x1)
print(x2)