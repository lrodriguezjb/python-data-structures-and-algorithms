a = [2, 4, 5, 10, 12, 18, 21, 30, 32, 54, 70, 76]


def binary_search(lst, val):
    left = 0
    right = len(lst)
    while left <= right:
        mid = left + (right - left)//2
        if lst[mid] == val:
            return mid
        elif lst[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return -1

