def function1(num1):
    x1 = 0
    for i in range(2,10):
        for k in range(1,10):
            for r in range(10):
                if r<1:
                    r = 0
                if k<2:
                    k = 0
                else:
                    k = (k*(k-1))//2
                if i<3:
                    i = 0
                else:
                    i = (i*(i-1)*(i-2))//6
                if num1 == i+k+r:
                    x1 = x1+1
                    break
            if x1 == 1:
                break
        if x1 == 1:
            print(int(str(i)+str(k)+str(r)))
            break
        
num1 = int(input())
x1 = []

for i in range(num1):
    x1.append(int(input()))
for i in range(len(x1)):
    function1(x1[i])


