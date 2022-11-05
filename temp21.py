x1 = input()
x2 = x1.split()
num1 = 0
num2 = 0
num3 = len(x2)
t1 = []
t2 = []
for i in x2:
    num1 = x2.count(i)
    if num1 > num2:
        num2 = num1
        k = i
        
    if num1 < num3:
        num3 = num1
        r = i


print(k,num2)
print(r,num3)

    
        
        
        
    