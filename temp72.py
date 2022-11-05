def convert(str):
    newstr = ''
    for i in range(len(str)):
        if(str[i] == 'W'):
            newstr = newstr+'sw3'
        elif(str[i] == 'X'):
            newstr = newstr+'sw2'
        elif(str[i] == 'Y'):
            newstr = newstr+'sw1'
        elif(str[i] == 'Z'):
            newstr = newstr+'sw0'
        else:
            newstr = newstr+str[i]
    return newstr

str = input()
newstr = convert(str)
print(newstr)
