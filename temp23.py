def  function1(num1):
    if num1>15:
        return
    k = 1
    for i in range(num1,0,-1):
        k = k*i
    return k

num1 = int(input())
print(function1(num1))