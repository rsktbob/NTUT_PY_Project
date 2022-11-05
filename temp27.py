def function1(x3):
    card = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':0.5,'Q':0.5,'K':0.5}
    return card[x3]
            
def function2():
    player=int(input())
    money=input().split()
    cardt=input().split()
    for i in range(player):
        x2=[]
        money[i]=int(money[i])
        x2.append(function1(cardt[i]))
        locals()['number'+str(i+1)]=function1(cardt[i])
        locals()['recard'+str(i+1)]=0
        locals()['recardt'+str(i+1)]=1
        while True:
            x1=input()
            if x1=='Y':
                x3=input()
                locals()['number'+str(i+1)]=locals()['number'+str(i+1)]+function1(x3)
                x2.append(function1(x3))
                if locals()['number'+str(i+1)]>10.5:
                    locals()['number'+str(i+1)]=0
                    break
                if locals()['number'+str(i+1)]<=10.5:
                    locals()['recardt'+str(i+1)]=locals()['recardt'+str(i+1)]+1
                if locals()['recardt'+str(i+1)]==5:
                   break
                if len(x2)==2:
                        if x2[0]==10:
                            if x2[1]==0.5:
                                locals()['recard'+str(i+1)]=1
                                break
                        if x2[0]==0.5:
                            if x2[1]==10:
                                locals()['recard'+str(i+1)]=1
                                break
            if x1=='N':
                break
    x3=input()
    spender=function1(x3)
    x1=0
    num1=0
    while spender!=0 and x1!='N':
        x1=input()
        if x1=='Y':
            x3=input()
            spender=spender+function1(x3)
        if spender>10.5:
            spender=0
    for i in range(player):
        if spender>=locals()['number'+str(i+1)] and locals()['recard'+str(i+1)]!=1 and locals()['recardt'+str(i+1)]!=5:
            print(f'Player{str(i+1)} -{str(money[i])}')
            num1=num1+money[i]
        if spender<locals()['number'+str(i+1)] or locals()['recard'+str(i+1)]==1 or locals()['recardt'+str(i+1)]==5:
            print(f'Player{str(i+1)} +{str(money[i])}')
            num1=num1-money[i]
    if num1>0:
        num1=abs(num1)
        print(f'Bank +{str(num1)}')
    if num1==0:
        num1=abs(num1)
        print(f'Bank {str(num1)}')
    if num1<0:
        num1=abs(num1)
        print(f'Bank -{str(num1)}')
    
function2()   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                    
                    
            


