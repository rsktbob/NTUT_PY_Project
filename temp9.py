def courseproduct(x1=[],x2=1):
    x1=[]
    x2=int(input())
    for i in range(x2):
        x1.append(input())
    
    return x1

def coursecompare(r1,r2,t1,t2):
    for i in range(len(r1)):
        for k in range(len(r2)):
            if  r1[i] == r2[k]:
                print(t1 + " and " + t2 + " on confict " + r2[k])
t1 = input()
r1 = courseproduct()
t2 = input()
r2 = courseproduct()
t3 = input()
r3= courseproduct()
coursecompare(r1,r2,t1,t2)
coursecompare(r2,r3,t2,t3)
coursecompare(r1,r3,t1,t3)
