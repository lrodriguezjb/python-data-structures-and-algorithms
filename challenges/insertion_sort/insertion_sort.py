def insertion_sort(list):
    """
    Takes in a list and sorts the list using an insertion sort method.
    """
    round_number = 1
    curr = round_number
    while round_number < len(list):
        while curr > 0:
            if list[curr] < list[curr - 1]:
                list[curr], list[curr - 1] = list[curr - 1], list[curr]
                curr -= 1
            else:
                break
        round_number += 1
        curr = round_number
    return list