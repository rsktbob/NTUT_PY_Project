import copy
def articleeditor():
    string1=input().split()
    articletimes=int(string1[0])
    commandtimes=int(string1[1])
    list1=[]
    list2=[]
    for i in range(articletimes):
        string1=input().split()
        list1.append(string1)
    for i in range(commandtimes):
        string1=input()
        list2.append(string1)
    for i in list2:
        if i[:11]=='ADD_W_FRONT':
            string1=i[12:]
            string1=string1.split()
            x1=int(string1[0])
            x2=int(string1[1])
            x3=string1[2:]
            for i in range(len(x3)-1,-1,-1):
                list1[x1-1].insert(x2-1,x3[i])
        elif i[:11]=='ADD_W_AFTER':
            string1=i[12:]
            string1=string1.split()
            x1=int(string1[0])
            x2=int(string1[1])
            x3=string1[2:]
            for i in range(len(x3)-1,-1,-1):
                list1[x1-1].insert(x2,x3[i])
        elif i[:11]=='ADD_S_FRONT':
            string1=i[12:]
            string1=string1.split()
            x1=int(string1[0])
            x2=string1[1:]
            for i in range(len(x2)-1,-1,-1):
                list1[x1-1].insert(0,x2[i])
        elif i[:11]=='ADD_S_AFTER':
            string1=i[12:]
            string1=string1.split()
            x1=int(string1[0])
            x2=string1[1:]
            for i in range(len(x2)):
                list1[x1-1].append(x2[i])
        elif i[:12]=='INSERT_FRONT':
            x1=i[13:]
            x1=x1.split()
            x2=x1[0]
            x3=x1[1]
            list3=copy.deepcopy(list1)
            for i in range(len(list3)):
                t1=0
                for k in range(len(list3[i])):
                    if list3[i][k]==x2:
                        list1[i].insert(k+t1,x3)
                        t1=t1+1
        elif i[:12]=='INSERT_AFTER':
            x1=i[13:]
            x1=x1.split()
            x2=x1[0]
            x3=x1[1]
            list3=copy.deepcopy(list1)
            for i in range(len(list3)):
                t1=0
                for k in range(len(list3[i])):
                    if list3[i][k]==x2:
                        list1[i].insert(k+t1+1,x3)
                        t1=t1+1
        elif i[:5]=='DEL_W':
            x1=int(i[6])
            x2=int(i[8])
            list1[x1-1].pop(x2-1)
        elif i[:5]=='DEL_L':
            x1=int(i[6])
            del list1[x1-1]
        elif i[:7]=='REPLACE':
            string1=i[8:]
            string1=string1.split()
            x1=string1[0]
            x2=string1[1]
            for i in range(len(list1)):
                for k in range(len(list1[i])):
                    if list1[i][k]==x1:
                        list1[i][k]=x2
        elif i[:5]=='COUNT':
            num1=0
            for i in range(len(list1)):
                for k in range(len(list1[i])):
                    num1=num1+1
            print(num1)
        string1=''
        list3=[]
        for k in range(len(list1)):
            string1=' '.join(list1[k])
            string1=string1.split()
            list3.append(string1)
        list1=list3
    for i in list1:
        print(' '.join(i))
 
      
articleeditor()       
    
