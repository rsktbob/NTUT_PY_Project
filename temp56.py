def university():
    string1=input().split()
    times1=int(string1[0])
    times2=int(string1[1])
    dict1={}
    for i in range(times1):
        string1=input().split()
        school=string1.pop(0)
        dict1[school]=string1
    return dict1,times2

def condition():
    dict1,times2=university()
    list1=[]
    for i in range(times2):
        string1=input().split(' + ')
        for i in range(len(string1)):
            string1[i]=string1[i].split()
        x1=[]
        for i in dict1:
            x2=0
            for k in string1:
                x3=0
                for t in range(len(k)):
                    if k[t] in dict1[i]:
                        x3=x3+1
                    elif k[t][0]=='!':
                        if k[t][1:] not in dict1[i]:
                            x3=x3+1
                if x3==len(k):
                    x2=x2+1
            x1.extend([i,x2])
        t1=[]
        for i in range(1,len(x1),2):
            if x1[i]!=0:
                t1.append([x1[i-1],x1[i]])
        t1.sort(key=lambda x:x[1],reverse=True)
        for i in range(len(t1)):
            for k in range(len(t1[i])):
                t1[i][k]=str(t1[i][k])
        for i in range(len(t1)):
            t1[i]=','.join(t1[i])
        t1=' '.join(t1)
        list1.append(t1)
    for i in list1:
        print(i)

        
condition()