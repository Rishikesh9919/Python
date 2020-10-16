import random

pos = -1


def linear_search(array, search_val):
    for ele in range(len(array)):
        if arr[ele] == search_val:
            global pos
            pos = ele + 1
            return True


# for generating 15 random numbers to sort
arr = [random.randint(1, 99) for i in range(15)]
print(arr)
search = int(input('Enter a value for search: '))
if linear_search(arr, search):
    print(search, ' is found at position ', pos)
else:
    print('The search value is not in the list')
