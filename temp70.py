import random,os

def check(ans_list,guess_list):
    A = 0
    B = 0
    for i in range(len(guess_list)):
        if(guess_list[i] == ans_list[i]):
            A = A+1
        elif(guess_list[i] in ans_list):
            B = B+1
    return A,B

ans_list = []
num1 = 0
while(len(ans_list) < 4):
    num1 = random.randint(0,9)
    if(num1 not in ans_list):
        ans_list.insert(0,num1)

while(True):
    guess = input()
    if(guess == "exit"):
        os._exit(0)
    guess = int(guess)
    guess_list = []
    for i in range(4):
        guess_list.insert(0,guess%10)
        guess = guess//10
    A ,B = check(ans_list,guess_list)
    if(A == 4):
        os._exit(0)
    else:
        print(f"{A} A,{B} B")


