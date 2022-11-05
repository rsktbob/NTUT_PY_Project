def makegraph():
    row,column=input().split()
    grath=[]
    for i in range(int(row)):
        columnnodes=input().split()
        grath.append(columnnodes)
    return grath

def testgraph(grath):
    prices={}
    for i in range(len(grath)):
        for k in range(len(grath[i])):
            total=0
            for t in range(len(grath)):
                for j in range(len(grath[t])):
                    row,column=abs(t-i),abs(j-k)
                    distance=row+column
                    amount=int(grath[t][j])
                    total=distance*amount+total
            prices[(i,k)]=total
    prices=prices.items()
    prices=list(prices)
    prices.sort(key=lambda x: x[1])
    return prices[0]

def information():
    times=int(input())
    saveprices=[]
    for i in range(times):
        grath=makegraph()
        pricesinformation=testgraph(grath)
        saveprices.append(pricesinformation)
    for i in range(times):
        for k in saveprices[i][0]:
            print(k+1,end=' ')
        print()
        print(saveprices[i][1]*100)
        
information()

      
        
            
    