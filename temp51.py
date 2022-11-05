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

def DFS():
    grath,friend1,friend2=makegrath()
    stack=[]
    list1=[]
    seen=set()
    stack.append(friend1)
    seen.add(friend1)
    while len(stack)>0:
        vertex=stack.pop()
        nodes=grath[vertex]
        for i in nodes:
            if i not in seen:
                stack.append(i)
                seen.add(i)
        list1.append(vertex)
    print(list1)

DFS()