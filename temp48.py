def makegrath():
    string=input().split()
    times=int(string[0])
    friend1=string[1]
    friend2=string[2]
    list1=[]
    dict1={}
    seen=set()
    for i in range(times):
        string=input().split()
        list1.append(string)
        for k in range(2):
            seen.add(string[k])
    for i in seen:
        x1=[]
        for k in range(times):
            if i in list1[k]:
                x1.extend(list1[k])
        while i in x1:
            x1.remove(i)
        dict1[i]=x1
    return dict1,friend1,friend2

def findrelation():
    grath,friend1,friend2=makegrath()
    queue=[]
    queue.append(friend1)
    list1=[]
    seen=set()
    seen.add(friend1)
    while len(queue)>0:
        vertex=queue.pop(0)
        nodes=grath[vertex]
        for i in nodes:
            if i not in seen:
                queue.append(i)
                seen.add(i)
        list1.append(vertex)
    if friend2 in list1:
        print('Yes!')
    else:
        print('No!')
        
findrelation()
    
    