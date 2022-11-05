data = input()
n = int(data.split()[0])
m = int(data.split()[1])

ans = 0
room = []
place = []

for i in range(n):
    data = input()
    room.append([data.split()[0], int(data.split()[1])])

for i in range(m):
    data = input()
    place.append([int(data.split()[0]), int(data.split()[1]), int(data.split()[2]), int(data.split()[3]), abs(int(data.split()[2])-int(data.split()[3]))])

place.sort(key = lambda x:x[4], reverse = True)

for i in range(1,pow(2, m)):
    placetest = [[False for x in range(24)] for y in range(n)]
    bin_str = str(bin(i))[2:].rjust(m, '0')
    count = 0
    for j in range(m):
        if(bin_str[j] == '0'):
            continue
        for k in range(n):
            flag = False
            if(place[j][1] > room[k][1]):
                continue
            for l in range(place[j][2], place[j][3]):
                flag = placetest[k][l] or flag
            if(flag == True):
                continue
            for l in range(place[j][2], place[j][3]):
                placetest[k][l] = True
            count += place[j][4]
            break
    ans = max(ans, count)

print(ans)

















