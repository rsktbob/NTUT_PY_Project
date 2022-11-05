def function1(num1):
    for i in range(num1):
        print(i)

def function2(num1,num2):
    print(num1*num2)
    for i in range(num1,num2):
        print(num1+i)

def function3(num1,num2):
    while num2!=0:
        num3=num1%num2
        num1=num2
        num2=num3
    return num1

def function4(list1):
    for i in range(len(list1)-1):
        for k in range(len(list1)-1-i):
            if list1[k]>list1[k+1]:
                list1[k],list1[k+1] = list1[k+1],list1[k]
    return list1
            

list1=[6,18,14,15,86,54]
print(function4(list1))




    

