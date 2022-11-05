x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())

a1 = x1*0.08 + x2*0.1393 + x3*0.1349 + x4*1.1287 + x5*1.4803
a2 = x1*0.07 + x2*0.1304 + x3*0.1217 + x4*1.1127 + x5*1.2458
a3 = x1*0.06 + x2*0.1087 + x3*0.1018 + x4*0.9572 + x5*1.1243

if a1<183:
    a1 = 183
    
if a2<383:
    a2 = 383

if a3<983:
    a3 = 983
    
if a1<a2 and a1<a3:
    print("Type 183")
elif a2<a1 and a2<a3:
    print("Type 383")
elif a3<a1 and a3<a2:
    print("Type 983")
    