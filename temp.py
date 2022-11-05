def function(card):
     pork = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
     point = [1,2,3,4,5,6,7,8,9,10,0.5,0.5,0.5]
     transplate = pork.index(card)
     return point[transplate]
 
def getsum(num1=1,num2=0,num3=1):
     num1 = input()
     num2 = input()
     num3 = input()
     totals = function(num1) + function(num2) + function(num3)
     return totals

def compare(num1,num2):
    if num1>num2 and num1<=10.5 or num1<=10.5 and num2>10.5:
       print("A WIN")
    elif num1<num2 and num2<=10.5 or num2<=10.5 and num1>10.5:
       print("B WIN")
    else:
        print("TIE")
     
num1 = getsum()
num2 = getsum()
compare(num1,num2)