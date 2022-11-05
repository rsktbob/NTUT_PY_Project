def function1(num1):
    for i in range(1,num1+1):
        print(i,end="")
        
def function2(num1):
    for i in range(num1-1,0,-1):
        print(i,end="")
        
def function3(num1):
    for i in range(num1-1,0,-1):
        print("_",end="")
        
def function4(num1):
    for i in range(1,num1+1):
        function1(i)
        function2(i)
        print()
        
def function5(num1):
    for i in range(1,num1+1):
        function3(num1-i+1)
        function1(i)
        function2(i)
        function3(num1-i+1)
        print()
  
def function6(num1):
    for i in range(num1,0,-1):
        function3(num1-i+1)
        function1(i)
        function2(i)
        function3(num1-i+1)
        print()


num1 = int(input())
num2 = int(input())
if num1 ==  1:
    function4(num2)
elif num1 == 2:
    function5(num2)
elif num1 == 3:
    function6(num2)