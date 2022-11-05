list1 = [5,  12, 54]
def function1(x1):
    for i in range(1,len(x1)):
        t = i
        for k in range(i-1,-1,-1):
            if x1[t]>=x1[k]:
                break
            else:
                x1[t],x1[k] = x1[k],x1[t]
                t = k
    print(x1)
    return x1

def function2(x1,x2,x3,list1):
    mid = (x1 + x2) // 2
    if list1[mid] == x3:
        print(mid+1)
        return
    elif x1 > x2:
        print('failed')
        return
    elif list1[mid] > x3:
        return function2(x1, mid-1, x3, list1)
    elif list1[mid] < x3:
        return function2(mid+1, x2, x3, list1)

def function3(x1,x2):
    x3 = 1
    while x3 != 0:
        x3 = x1 % x2
        x1 = x2
        x2 = x3
    print(x1)

def function4(left,right,list1):
    if left >= right:
        return
    i = left
    j = right
    key = i
    while i != j:
        while list1[i] < list1[key] and i < j:
            i = i + 1
        while list1[j] >= list1[key] and i < j:
            j = j - 1
        list1[i],list1[j] = list1[j],list1[i]
    list1[key],list1[i] = list1[key],list1[i]
    function4(left, i-1, list1)
    function4(i+1, right, list1)

def function5():
    times = int(input())
    list1 = []
    element = set()
    dict1 = {}
    for i in range(times):
        nodes = input().split()
        list1.append(nodes)
    for i in list1:
        for k in range(2):
            element.add(i[k])
    for i in element:
        dict1[i] = set()
        for k in list1:
            if i in k:
                for t in k:
                    dict1[i].add(t)
        dict1[i].remove(i)
    return dict1

def function6(dict1):
    start,end = input().split()
    queue = []
    grath = []
    seen = set()
    queue.append(start)
    grath.append([start])
    seen.add(start)
    while len(queue) != 0:
        node = queue.pop(0)
        for i in grath:
            if i[-1] == node:
                x1 = i
        for i in dict1[node]:
            if i not in seen:
                queue.append(i)
                seen.add(i)
                x2 = x1.copy()
                x2.append(i)
                grath.append(x2)
    return grath

class Cars():
    def __init__(self,*x1):
        self.color=x1[0]
        self.seat=x1[1]
        self.emergency=x1[2]
        self.ability=x1[3]
    def drive(self,x1):
        print(x1)
        print(self.emergency)
    def information(self):
        print(self.color,self.seat,self.ability)
    def init(self):
        self.color='blue'
        self.seat=3
        self.emergency=80
        self.ability='no ability'

class plastic():
    def __init__(self,*element):
        self.color=element[0]
        self.space=element[1]
        self.ability=element[2]

    def function1(self):
        print(self.space)

    def function2(self):
        print(self.color,self.ability)

x1=plastic(3,6,8)
x1.function1()







