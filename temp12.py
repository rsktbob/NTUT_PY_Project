def mylower(str1):
    str2 = str1.lower()
    k = 0
    t = 0
    for i in str1:
        if i == str2[k] and i.islower():
            print(i,end="")
            t = t+1
        k = k+1
    if t == 0:
        print("No lowercase letters")

def myupper(str1):
    str2 = str1.upper()
    k = 0
    t = 0
    for i in str1:
        if i == str2[k] and i.isupper():
            t = t+1
        k = k+1
    return t




str1 = input()
mylower(str1)
print()
print(len(str1))
print(myupper(str1))
    