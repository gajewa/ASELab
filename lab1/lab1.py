import random
import time
import copy


# unsortedList = random.sample(range(100), 1000)
firstList = [random.randrange(1, 3) for _ in range(0, 5000)]
secondList = copy.copy(firstList)
thirdList = copy.copy(firstList)

def bubbleSort(unsortedList):
    ready = False

    while not ready:
        ready = True
        for i in range(len(unsortedList)-1):
            if unsortedList[i] > unsortedList[i+1]:
                unsortedList[i], unsortedList[i+1] = unsortedList[i+1], unsortedList[i]
                ready = False
                break

    return unsortedList


def selectionSort(unsortedList):
    for i in range(len(unsortedList)):
        minimum = 100
        minimumIndex = 0
        for j in range(i, len(unsortedList)):
            if unsortedList[j] < minimum:
                minimum = unsortedList[j]
                minimumIndex = j
        unsortedList[i], unsortedList[minimumIndex] = unsortedList[minimumIndex], unsortedList[i]

    return unsortedList

def quickSort(unsortedList):

    if not unsortedList:
        return []

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

print('Unsorted list:' )
print(firstList)

start = time.time()
bubbleList = bubbleSort(firstList)
end = time.time()
bubbleTime = end - start
# print(firstList)

start = time.time()
selectionList = selectionSort(secondList)
end = time.time()
selectionTime = end - start

start = time.time()
quickList = quickSort(thirdList)
end = time.time()
quickTime = end - start


print('Sorted with bubblesort in ' + str(bubbleTime) + ' s: ')
print(bubbleList)
print('Sorted with selectionsort in ' + str(selectionTime) + ' s : ')
print(selectionList)
print('Sorted with bubblesort in ' + str(quickTime) + ' s :')
print(quickList)
