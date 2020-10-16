import random


def selection_sort(array):
    for i in range(len(array) - 1):
        min_val_pos = i
        for j in range(i, len(array)):
            if arr[j] < arr[min_val_pos]:
                min_val_pos = j
        array[i], array[min_val_pos] = array[min_val_pos], array[i]


arr = [random.randint(1, 99) for i in range(15)]
print('Before sorting: ', arr)
selection_sort(arr)
print('After Sorting:  ', arr)
