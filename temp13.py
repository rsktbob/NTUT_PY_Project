def function1():
    num1 = int(input())
    k = []
    for i in range(num1):
        k.append(int(input()))
        k.sort()
    return k[num1-2],k[0]*k[num1-1]
        
num1,num2 = function1()
print(num1)
print(num2)