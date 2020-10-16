import random


def selection_sort(array):
    for i in range(len(array) - 1):
        # to keep track of position of minimum value
        min_val_pos = i
        for j in range(i, len(array)):
            if arr[j] < arr[min_val_pos]:
                min_val_pos = j
        # Swapping with the minimum number from the list
        array[i], array[min_val_pos] = array[min_val_pos], array[i]


# for generating 15 random numbers to sort 
arr = [random.randint(1, 99) for i in range(15)]
print('Before sorting: ', arr)
selection_sort(arr)
print('After Sorting:  ', arr)
