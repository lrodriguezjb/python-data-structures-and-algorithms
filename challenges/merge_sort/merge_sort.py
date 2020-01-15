def merge_sort(list):
    """
    Takes in a list and sorts it using merge sort logic. Returns the list.
    """
    if len(list) <= 1:
        print(list)
        return list

    mid = len(list) // 2
    left_slice = list[:mid]
    right_slice = list[mid:]

    left = merge_sort(left_slice)
    right = merge_sort(right_slice)

    def _merge_sort(list_one, list_two):
        """
        Merges two lists together, sorting them as it assembles a new list and then returns the new list.
        """
        output = []
        count_one = 0
        count_two = 0

        while count_one < len(list_one) and count_two < len(list_two):
            if list_one[count_one] < list_two[count_two]:
                output.append(list_one[count_one])
                count_one += 1
            else:
                output.append(list_two[count_two])
                count_two += 1

        output += list_one[count_one:]
        output += list_two[count_two:]

        return output

    return _merge_sort(left, right)
