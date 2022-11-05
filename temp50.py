def receipt():
    x1=[]
    for i in range(4):
        x1.append(input().split())
    return x1

def checkreceipt():
    dict1=receipt()
    times=int(input())
    x1=0
    x2=[200000,40000,10000,4000,1000,200]
    for i in range(times):
        string1=input()
        x3=0
        t1=0
        if string1==dict1[0][0]:
            x1=x1+10000000
            x3=1
        elif string1==dict1[1][0]:
            x1=x1+2000000
            x3=1
        if x3==0:
            for i in range(len(x2)):
                for k in range(3):
                    if string1[i:]==dict1[2][k][i:]:
                        x1=x1+x2[i]
                        t1=1
                        break
                if t1==1:
                    break
        if t1==0 and x3==0:
            if string1[5:] in dict1[3]:
                x1=x1+200
    print(x1)
 
checkreceipt()            
            

