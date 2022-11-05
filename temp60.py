data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

def SelectionSort(data):
	begin = 0
	for i in range(len(data)-1):
		for k in range(len(data)-1,begin-1,-1):
			print(k)
			if data[begin] > data[i]:
				x1 = 0
				exchange = i
				break
			elif i == begin:
				x1 = 1
		if x1 == 0:
			data[begin], data[exchange] = data[exchange], data[begin]
			begin = begin + 1
	return data



print(SelectionSort(data))