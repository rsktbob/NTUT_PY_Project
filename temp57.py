def game():
    grath = [0 for i in range(9)]
    playerstart = input()
    string1 = input().split()
    string1 = considergame(string1)
    key1 = 0
    key2 = 0
    if playerstart == '1':
        for i in range(len(string1)):
            t = int(string1[i])
            if grath[t-1] != 2 and i % 2 == 0:
                grath[t-1] = 1
            elif grath[t-1] != 1 and i % 2 == 1:
                grath[t-1] = 2
            key1,key2 = judgevictory(grath,key1,key2)
            if key1 == 1:
                grath = list(map(str,grath))
                print(' '.join(grath[:3]))
                print(' '.join(grath[3:6]))
                print(' '.join(grath[6:]))
                print('Player win')
                break
            elif key2 == 1:
                grath = map(str, grath)
                grath = list(map(str,grath))
                print(' '.join(grath[:3]))
                print(' '.join(grath[3:6]))
                print(' '.join(grath[6:]))
                print('Computer win')
                break
    elif playerstart == '2':
        for i in range(len(string1)):
            t = int(string1[i])
            if grath[t-1] != 1 and i % 2 == 0:
                grath[t-1] = 2
            elif grath[t-1] != 2 and i % 2 == 1:
                grath[t-1] = 1
            key1,key2 = judgevictory(grath,key1,key2)
            if key1 == 1:
                grath = list(map(str,grath))
                print(' '.join(grath[:3]))
                print(' '.join(grath[3:6]))
                print(' '.join(grath[6:]))
                print('Player win')
                break
            elif key2 == 1:
                grath = list(map(str, grath))
                print(' '.join(grath[:3]))
                print(' '.join(grath[3:6]))
                print(' '.join(grath[6:]))
                print('Computer win')
                break
    if key1 == 0 and key2 == 0:
        if 0 not in grath:
            grath = list(map(str, grath))
            print(' '.join(grath[:3]))
            print(' '.join(grath[3:6]))
            print(' '.join(grath[6:]))
            print('Tie')
        elif key1 == 0 and 0 in grath and key2 == 0 and 0 in grath:
            grath = list(map(str, grath))
            print(' '.join(grath[:3]))
            print(' '.join(grath[3:6]))
            print(' '.join(grath[6:]))
            print('Undecided')
            grath = list(map(int, grath))
            judgestep(grath)



def considergame(string1):
     key = 0
     list1 = []
     for i in string1:
         if string1.count(i) > 1:
             print('Error')
             key = 1
             break
     if key == 0:
         print('OK')
     for i in string1:
         if i not in list1:
             list1.append(i)
     return list1



def judgevictory(grath,key1,key2):
     x1 = (0, 3, 6, 0, 1, 2, 0, 2)
     x2 = (1, 4, 7, 3, 4, 5, 4, 4)
     x3 = (2, 5, 8, 6, 7, 8, 8, 6)
     for i in range(8):
         string1 = [grath[x1[i]], grath[x2[i]], grath[x3[i]]]
         if string1.count(1) == 3:
             key1 = 1
             break
         elif string1.count(2) == 3:
             key2 = 1
             break
     return key1,key2

def judgestep(grath):
     x1 = (0, 3, 6, 0, 1, 2, 0, 2)
     x2 = (1, 4, 7, 3, 4, 5, 4, 4)
     x3 = (2, 5, 8, 6, 7, 8, 8, 6)
     t1 = []
     t2 = []
     k1 = []
     k2 = []
     k3 = []
     for i in range(8):
         if [grath[x1[i]], grath[x2[i]], grath[x3[i]]].count(1) == 2 and [grath[x1[i]], grath[x2[i]], grath[x3[i]]].count(0) == 1:
               list1 = [x1[i], x2[i], x3[i]]
               key =  [grath[x1[i]], grath[x2[i]], grath[x3[i]]].index(0)
               t1.append(list1[key] + 1)
         if  [grath[x1[i]], grath[x2[i]], grath[x3[i]]].count(2) == 2  and  [grath[x1[i]], grath[x2[i]], grath[x3[i]]].count(0) == 1:
                list2 = [x1[i], x2[i], x3[i]]
                key =  [grath[x1[i]], grath[x2[i]], grath[x3[i]]].index(0)
                t2.append(list2[key]+1)
     for i in range(1,10):
         if i in t1 and i in t2:
             k1.append(i)
         elif i in t1:
             k2.append(i)
         elif i in t2:
             k3.append(i)
     if len(k1) != 0:
        print(k1[0])
     elif len(k2) != 0:
        print(k2[0])
     elif len(k3) != 0:
        print(k3[0])

game()


















