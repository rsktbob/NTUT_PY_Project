def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if (list[j] > list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]

def select_sort(list):
    for i in range(len(list) - 1):
        key = i
        for j in range(i, len(list)):
            if (list[key] > list[j]):
                key = j
        list[i], list[key] = list[key], list[i]

list1  = [6,2,4,3,24,1]
str1 = "dsfsdfadsft"
str1[0] = 't'
print(str1)