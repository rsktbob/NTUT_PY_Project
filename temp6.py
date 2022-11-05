sentence1 = input()
sentence2 = input()
x1 = input()
x2 = input()

c = sentence1 + sentence2
d = c.replace(x1,x2)
print(len(c+d))
e = d[0:3] + d[-3:]
print(e*3)

  
