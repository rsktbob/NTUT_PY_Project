import random

given_number = random.randint(0,1000000000000)
difference = 0
M = 0
m = 0
list = []
num1 = given_number
while(num1 > 0):
    list.append(num1%10)
    num1 = num1//10

if(list):
    list.sort()
    j = 1
    for i in range(len(list)):
        M = M+list[i]*j
        m = m+list[len(list)-i-1]*j
        j = j*10
        
difference = M-m
print(given_number)
print(difference)
print(M)
print(m)


