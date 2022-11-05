def function1(num1):
    for i in range(num1,0,-1):
        print(i,end="")
        
def function2(num1):
    for i in range(num1):
        print("#",end="")

def function3(num1):
    for i in range(num1,0,-1):
        function2(num1*2-i)
        function1(i)
        print()

num1 = int(input())
function3(num1)