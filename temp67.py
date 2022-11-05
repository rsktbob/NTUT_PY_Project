import random

A = list(set([random.randint(0,99) for i in range(20)]))
B = list(set([random.randint(0,99) for i in range(20)]))
common = []
for i in A:
    if(i in B):
        common.append(i)
result = common
print(A)
print(B)
print(common)