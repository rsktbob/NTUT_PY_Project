def myprint(mark,num1):
    for i in range(num1):
        print(mark,end="")
        
def myprints(num1):
    for i in range(1,(num1+1)//2+1):
        myprint("*",i)
        print()
    for k in range((num1-1)//2,0,-1):
        myprint("*",k)
        print()

def myprintr(num1):
    for i in range(1,(num1+1)//2+1):
        myprint(".",(num1+1)//2-i)
        myprint("*",i)
        print()
    for k in range((num1-1)//2,0,-1):
        myprint(".",(num1-1)//2+1-k)
        myprint("*",k)
        print()
        
def myprintn(num1):
    for i in range(1,num1+1,2):
        myprint(".",(num1+1)//2-(i+1)//2)
        myprint("*",i)
        print()
    for k in range(num1-2,0,-2):
        myprint(".",(num1+1)//2-(k+1)//2)
        myprint("*",k)
        print()
                
        
num1 = int(input())
num2 = int(input())
if num1 == 1:
   myprints(num2)
elif num1 == 2:
   myprintr(num2)
elif num1 == 3:
   myprintn(num2)
  
    