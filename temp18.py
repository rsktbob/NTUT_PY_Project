def function1(num1):
    if num1 == 2:
        print(f"{num1} is prime number")
        return
    elif num1 == 1:
        print(f"{num1} is not prime number")
        return
    for i in range(2,num1):
        if num1 % i == 0 :
            print(f"{num1} is not prime number")
            break
    if i == num1-1 and num1 % i != 0:
        print(f"{num1} is prime number")
    
num1 = int(input())
if num1 <= 200:
    function1(num1)

