def function1():
    num1=input().split(',')
    return int(num1[0]),int(num1[1])

def function2():
    num1=int(input())
    x1=[]
    for i in range(num1):
        x1.append(function1())
    for i in range(len(x1)-1):
        k=i+1
        while k<=len(x1)-1:
            if x1[i][0]<=x1[k][0] and x1[i][1]>=x1[k][1]:
                x1.remove(x1[k])
                k=i
            elif x1[i][0]>=x1[k][0] and x1[i][1]<=x1[k][1]:
                 x1.remove(x1[i])
                 k=i
            elif x1[i][0]<=x1[k][0]<=x1[i][1]<=x1[k][1]:
                  x1[i]=[x1[i][0],x1[k][1]]
                  x1.remove(x1[k])
                  k=i
            elif x1[k][0]<=x1[i][0]<=x1[k][1]<=x1[i][1]:
                  x1[k]=[x1[k][0],x1[i][1]]
                  x1.remove(x1[i])
                  k=i
            k=k+1
    for i in range(len(x1)):
        print(f'{x1[i][0]},{x1[i][1]}')
    
function2()