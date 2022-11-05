def covert(str,list):
    newstr = ""
    j=0
    for i in str:
        if(j==0):
            newstr = newstr + '('
        if(i==' '):
            newstr = newstr + " OR "
        if(newstr!="" and newstr[-1]!=' ' and newstr[-1]!='(' and i!='2'):
            newstr = newstr + " AND "
        if(i=='1'):
            newstr = newstr + list[j]
        elif(i=='0'):
            newstr = newstr + f"(NOT {list[j]})"
        if(j==3):
            newstr = newstr + ')'
        j=j+1
        j=j%5
    return newstr

list = ['W','X','Y','Z']
str = input()
newstr = covert(str,list)
print(newstr)