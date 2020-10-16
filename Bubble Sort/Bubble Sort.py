import random


def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if arr[j] >= arr[j + 1]:
                # Swapping with the minimum number from the list
                array[j], array[j + 1] = array[j + 1], array[j]


# for generating 15 random numbers to sort
arr = [random.randint(1, 99) for i in range(15)]
print('Before sorting: ', arr)
bubble_sort(arr)
print('After Sorting:  ', arr)
