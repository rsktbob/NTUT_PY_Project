def function1(num1,num2):
    if num1%2 == 1:
        num1 = num1+1
    if num2%2 == 1:
        num2 = num2-1
    k = 0
    for i in range(num1,num2+1,2):
        k = k+i
    return k

num1 = int(input())
num2 = int(input())
print(function1(num1,num2))
