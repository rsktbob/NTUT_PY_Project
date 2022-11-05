def function1(card2):
    for i in range(1,18):
        if card2.count(i)==2:
            return 1
        
def function2(card2):
    num1=0
    for i in range(1,18):
        if card2.count(i)==2:
            num1=num1+1
    if num1==2:
        return 1
    
def function3(card2):
    for i in range(1,18):
        if  card2.count(i)==3:
            return 1

def function4(card2):
    num1=0
    card2.sort()
    for i in range(0,4):
        if card2[i]==card2[i+1]-1:
            num1=num1+1
    if num1==4:
        return 1
    for i in range(5):
        if card2[i]==1 or card2[i]==2 or card2[i]==3 or  card2[i]==4:
            card2[i]=card2[i]+13
    num1=0
    card2.sort()
    for i in range(4):
        if card2[i]==card2[i+1]-1:
            num1=num1+1
    if num1==4:
        return 1
    
def function5(card1):
    num1=0
    for i in range(4):
        if card1[i][-1]==card1[i+1][-1]:
            num1=num1+1
    if num1==4:
        return 1
   
def function6(card2):
    for i in range(1,18):
        if  card2.count(i)==2:
            for k in range(i+1,18):
                if  card2.count(k)==3:
                    return 1
        if  card2.count(i)==3:
            for k in range(i+1,18):
                if  card2.count(k)==2:
                    return 1
       
def function7(card2):
    for i in range(1,18):
        if  card2.count(i)==4:
            return 1
            
def function8(card1,card2):
    num1=0
    num2=0
    for i in range(4):
        if card1[i][1]==card1[i+1][1]:
            num1=num1+1
    if num1==4:
        card2.sort()
        for i in range(4):
            if card2[i]==card2[i+1]-1:
                num2=num2+1
        if num2==4:
            return 1
        for i in range(5):
            if card2[i]==1 or card2[i]==2 or card2[i]==3 or  card2[i]==4:
                card2[i]=card2[i]+13
        num2=0
        card2.sort()
        for i in range(4):
            if card2[i]==card2[i+1]-1:
                num2=num2+1
        if num2==4:
           return 1
        
card3={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
    

cardpoint={}
for i in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
    for k in "SHDC":
        card=str(i)+k
        cardpoint[card]=card3[i]
          
def cardnumber():
    card1=input().split()
    card2=[]
    for i in card1:
        card2.append(cardpoint[i])
    if function8(card1,card2)==1:
        return 8
    elif function7(card2)==1:
        return 7
    elif function6(card2)==1:
        return 6
    elif function5(card1)==1:
        return 5
    elif function4(card2)==1:
        return 4
    elif function3(card2)==1:
        return 3
    elif function2(card2)==1:
        return 2
    elif function1(card2)==1:
        return 1
    else:
        return 0
 
print(cardnumber())












