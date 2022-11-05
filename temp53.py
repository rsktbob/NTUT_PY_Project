from itertools import combinations
def makemeeting():
    string1=input().split()
    meetingroom=int(string1[0])
    times=int(string1[1])
    list1=[[0]*24 for i in range(meetingroom)]
    list2=[]
    x1=''
    num1=0
    dict1={}
    for i in range(times):
        string1=input().split()
        x2=int(string1[1])
        x3=int(string1[2])
        dict1[string1[0]]=[x2,x3]
    for i in range(1,times+1):
        list2.extend(list(combinations(list(dict1.keys()),i)))
    for i in list2:
        t1=0
        num2=0
        list1=init(list1)
        for k in i:
            x2,x3=dict1[k]
            for t in list1:
                if t[x2:x3]==[0]*(x3-x2):
                    t[x2:x3]=[1]*(x3-x2)
                    t1=t1+1
                    break
        if t1==len(i):
            for g in i:
                x2,x3=dict1[g]
                num2=num2+x3-x2
            if num1<num2:
                num1=num2
    print(num1)
            
def init(list1):
    for i in range(len(list1)):
        for k in range(24):
            if list1[i][k]!=0:
                list1[i][k]=0
    return list1
              
makemeeting()

