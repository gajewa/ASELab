import random

# unsortedList = random.sample(range(100), 1000)
unsortedList = [random.randrange(1, 5) for _ in range(0, 5)]

def bubbleSort():
    ready = False

    while not ready:
        ready = True
        for i in range(len(unsortedList)-1):
            if unsortedList[i] > unsortedList[i+1]:
                unsortedList[i], unsortedList[i+1] = unsortedList[i+1], unsortedList[i]
                ready = False


def selectionSort():
    for i in range(len(unsortedList)):
        minimum = 100
        minimumIndex = 0
        for j in range(i, len(unsortedList)):
            if unsortedList[j] < minimum:
                minimum = unsortedList[j]
                minimumIndex = j
        unsortedList[i], unsortedList[minimumIndex] = unsortedList[minimumIndex], unsortedList[i]

def quickSort(unsortedList):

    if(not unsortedList):
        return

    lesser = []
    greater = []
    pivots = []

    for x in unsortedList:
        if x > unsortedList[0]:
            greater.append(x)
        elif x < unsortedList[0]:
            lesser.append(x)
        else:
            pivots.append(x)

    return quickSort(lesser) + pivots + quickSort(greater)

newList = quickSort(unsortedList)

# a = [1 , 2]
# b = [3 , 4 ]
# c = [5 , 6]
#
# d = a + b + c

# a.append(b)
# a.append(c)
# print(d)
#
print(newList)

# print(unsortedList)