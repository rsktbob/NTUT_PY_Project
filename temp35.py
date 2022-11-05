def function1(data,left,right):
    if left>=right:
        return
    i=left
    j=right
    key=data[left]
    while i<j:
        while data[j]>=key and i<j:
            j=j-1
        while data[i]<=key and i<j:
            i=i+1
        if i<j:
            data[i],data[j]=data[j],data[i]

    data[i],data[left]=data[left],data[i]
    function1(data,left,i-1)
    function1(data,i+1,right)
   
data=[65,43,52,48,21,14,84,24,18,45] 
function1(data,0,len(data)-1)           
print(data)