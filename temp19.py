x1 = []
x2 = []
def function1(num1,num2,x1,x2):
    x2[num1] = x1[num2]
    
def function2(num1,num2,x1,x2):
    x1[num1] = x2[num2]
    
def function3(num1,num2,num3,x1):
     x1[num1] = x1[num2] + x1[num3]
    
def function4(num1,num2,x1):
    x1[num1] = x1[num2]

for i in range(8):
    x1.append(int(input()))
for i in range(4):
    x2.append(0)


num1 = int(input())
for i in range(num1):
    t1,t2,*t3 = input().split()
    t2 = int(t2)
    for i in range(len(t3)):
        t3[i] = int(t3[i])
    if t1 == "LOAD":
        function1(t2,t3[0],x1,x2)
    elif t1 == "STORE":
        function2(t2,t3[0],x1,x2)
    elif t1 == "ADD":
        function3(t2,t3[0],t3[1],x2)
    elif t1 == "MOVE":
        function4(t2,t3[0],x2)
        
print(x2[0])
print(x1[0])
    
        

        
        
    



    
    
    

    
