def makegrath():
    string1=input().split()
    times=int(string1[0])
    start=string1[1]
    interesting=string1[2]
    end=string1[3]
    num1=0
    list1=[]
    element=set()
    grath1=[]
    dict1={}
    for i in range(times):
        string1=input().split()
        list1.append(string1)
        element.add(string1[0])
        element.add(string1[1])
    for i in element:
        x1=[]
        for k in list1:
            if i in k:
                x1.extend(k)
        x1=list(set(x1))
        dict1[i]=x1
    dict2=dict1.copy()
    if end in list(dict2.keys()):
        del dict2[end]
    else:
         print('No way!')
    for i in dict2:
        t1=dict2[i].copy()
        while end in t1:
            t1.remove(end)
        dict2[i]=t1
    queue=[]
    seen=set()
    queue.append(start)
    seen.add(start)
    grath1.append([start])
    while len(queue)>0:
        vertex=queue.pop(0)
        nodes=dict2[vertex]
        for i in grath1:
            if i[-1]==vertex:
                visited1=i.copy()
                grath1.remove(i)
        for i in nodes:
            if i not in seen:
                queue.append(i)
                seen.add(i)
                vicited2=visited1.copy()
                vicited2.append(i)
                grath1.append(vicited2)                
        for i in grath1:
            if i[-1]==interesting:
                num1=1
                break
        if num1==1:
            break
    grath2=[]
    for i in grath1:
        if i[-1]==interesting:
            grath2.append(i)
    if len(grath2)==0:
        print('No way!')
        return
    x1=grath2[0]
    x1.remove(interesting)
    for i in x1:
        del dict1[i]
    for i in dict1:
        t1=dict1[i].copy()
        for k in x1:
            if k in t1:
                t1.remove(k)
        dict1[i]=t1
    queue.clear()
    seen.clear()
    newgrath1=[]
    queue.append(interesting)
    seen.add(interesting)
    newgrath1.append([interesting])
    while len(queue)>0:
        vertex=queue.pop(0)
        nodes=dict1[vertex]
        for i in newgrath1:
            if i[-1]==vertex:
                visited1=i.copy()
                newgrath1.remove(i)
        for i in nodes:
            if i not in seen:
                queue.append(i)
                seen.add(i)
                vicited2=visited1.copy()
                vicited2.append(i)
                newgrath1.append(vicited2)                
        for i in newgrath1:
            if i[-1]==end:
                num1=0
                break
        if num1==0:
            break
    newgrath2=[]
    for i in newgrath1:
        if i[-1]==end:
            newgrath2.append(i)
    if len(newgrath2)==0:
        print('No way!')
        return
    else:
        x2=newgrath2[0]
        x1.extend(x2)
        print(len(x1)-1)
        x1='-'.join(x1)
        print(x1)
    
makegrath()

                
                

                
            
    
          
    
 
             
    


                     
                 
    
            
                    
    
    
    
    
        