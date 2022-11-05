x1 = input()
p = input()
q = input()


x2 = x1.split()
a = x2.index(p)
x2[a] = q
b = x2.index(p)
x2[b] = q
x2 = " ".join(x2)
x3 = list(filter((p).__ne__, x1.split()))
x3 = " ".join(x3)

print(x2)
print(x3)

