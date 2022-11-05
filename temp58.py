import copy
def ADD_W_FRONT(i, n, word, list1):
	list1[i-1].insert(n-1,word)
	return list1

def ADD_W_AFTER(i, n, word, list1):
	list1[i-1].insert(n,word)
	return list1

def ADD_S_FRONT(i, word, list1):
	for k in word[-1::-1]:
		list1[i-1].insert(0, k)
	return list1

def ADD_S_AFTER(i, word, list1):
	list1[i-1].extend(word)
	return list1

def INSERT_FRONT(key, word, list1):
	list2 = copy.deepcopy(list1)
	for i in range(len(list2)):
		if key in list2[i]:
			t = 0
			for k in range(len(list2[i])):
				if list2[i][k] == key:
					list1[i].insert(k+t, word)
					t = t + 1
	return list1

def INSERT_AFTER(key, word, list1):
	list2 = copy.deepcopy(list1)
	for i in range(len(list2)):
		if key in list2[i]:
			t = 0
			for k in range(len(list2[i])):
				if list2[i][k] == key:
					list1[i].insert(k+t+1, word)
					t = t + 1
	return list1

def DEL_W(i, n, list1):
	list1[i-1].pop(n-1)
	return list1

def DEL_L(i, list1):
	list1.pop(i-1)
	return list1

def REPLACE(old, new, list1):
	for i in list1:
		if old in i:
			for k in range(len(i)):
				if i[k] == old:
					i[k] = new
	return list1

def COPY_L(i, list1):
	list2 = list1[i-1].copy()
	return list2

def COPY(i, n, list1):
	list2 = [list1[i-1][n-1]]
	return list2

def PASTE_FRONT(i, n, list1, list2):
	for k in list2[-1::-1]:
		list1[i-1].insert(n-1, k)
	return list1

def PASTE_AFTER(i, n, list1, list2):
	for k in list2[-1::-1]:
		list1[i-1].insert(n, k)
	return list1


def COUNT(list1):
	times = 0
	for i in list1:
		for k in i:
			times = times + 1
	print(times)

def information():
	article, times = input().split()
	article = int(article)
	times = int(times)
	list1 = []
	list2 = 0
	for i in range(article):
		string1 = input().split()
		list1.append(string1)
	for i in range(times):
		string1 = input().split()
		string2 = string1[0]
		if string2 == 'ADD_W_FRONT':
			i, n, word = int(string1[1]), int(string1[2]), string1[3]
			list1 = ADD_W_FRONT(i, n, word, list1)
		elif string2 == 'ADD_W_AFTER':
			i, n, word = int(string1[1]), int(string1[2]), string1[3]
			list1 = ADD_W_AFTER(i, n, word, list1)
		elif string2 == 'ADD_S_FRONT':
			i, word = int(string1[1]), string1[2:]
			list1 = ADD_S_FRONT(i,  word, list1)
		elif string2 == 'ADD_S_AFTER':
			i, word = int(string1[1]), string1[2:]
			list1 = ADD_S_AFTER(i,  word, list1)
		elif string2 == 'INSERT_FRONT':
			key, word = string1[1], string1[2]
			list1 = INSERT_FRONT(key, word, list1)
		elif string2 == 'INSERT_AFTER':
			key, word = string1[1], string1[2]
			list1 = INSERT_AFTER(key, word, list1)
		elif string2 == 'DEL_W':
			i, n = int(string1[1]), int(string1[2])
			list1 = DEL_W(i, n, list1)
		elif string2 == 'DEL_L':
			i = int(string1[1])
			list1 = DEL_L(i, list1)
		elif string2 == 'REPLACE':
			old, new = string1[1], string1[2]
			list1 = REPLACE(old, new, list1)
		elif string2 == 'COPY_L':
			i = int(string1[1])
			list2 = COPY_L(i, list1)
		elif string2 == 'COPY':
			i, n = int(string1[1]), int(string1[2])
			list2 = COPY(i, n, list1)
		elif string2 == 'PASTE_FRONT':
			i, n = int(string1[1]), int(string1[2])
			list1 = PASTE_FRONT(i, n, list1, list2)
		elif string2 == 'PASTE_AFTER':
			i, n = int(string1[1]), int(string1[2])
			list1 = PASTE_AFTER(i, n, list1, list2)
		elif string2 == 'COUNT':
			COUNT(list1)
	for i in list1:
		string1 = ' '.join(i)
		print(string1)


information()






