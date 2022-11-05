def makegrath():
    string1=input().split()
    times=int(string1[0])
    start=string1[1]
    end=string1[2]
    list1=[]
    element=set()
    grath={}
    for i in range(times):
        string1=input().split()
        list1.append(string1)
    for i in list1:
        for k in range(2):
            element.add(i[k])
    for i in element:
        x1=[]
        for k in list1:
            if i in k:
                x2=list(filter(lambda x:x!=i,k))
                x2=x2[0]
                x1.append(x2)
        grath[i]=x1
    return grath,start,end

def BFS():
    grath,start,end=makegrath()
    queue=[]
    visited1=[]
    seen=set()
    queue.append(start)
    visited1.append([start])
    seen.add(start)
    while len(queue)>0:
        vertex=queue.pop(0)
        nodes=grath[vertex]
        for i in visited1:
            if i[-1]==vertex:
                visited2=i
        for i in nodes:
            if i not in seen:
                queue.append(i)
                seen.add(i)
                visited3=visited2.copy()
                visited3.append(i)
                visited1.append(visited3)
                if i==end:
                    return visited1[-1]
 
print(BFS())   

         
            
        
        