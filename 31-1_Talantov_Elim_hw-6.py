def bubble(lst):
    a = len(lst)
    for i in range(a):
        for b in range(a - i - 1):
            if lst[b] > lst[b + 1]:
                lst[b], lst[b + 1] = lst[b + 1], lst[b]
    return lst

list = [123, 12345, 12, 1, 1234]
sorted = bubble(list)
print(sorted)

def binary_search(element, lst):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if guess == element:
            return mid
        elif guess > element:
            high = mid - 1
        else:
            low = mid + 1

    return -1

my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
element_to_find = 12

result = binary_search(element_to_find, my_list)

if result != -1:
    print("Элемент найден на позиции", result)
else:
    print("Элемент не найден")