def mysum(num1,num2):
    k = 0
    for i in range(num1,num2+1,2):
        k = k+i
    return k

def myproduction(num1,num2):
    k = 1
    for i in range(num1,num2+1,3):
        k = k*i
    return k



num1 = int(input())
num2 = int(input())
print(mysum(num1,num2))
print(myproduction(num1,num2))