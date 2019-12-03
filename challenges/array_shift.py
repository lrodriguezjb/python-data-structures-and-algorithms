a = [1, 2, 3, 4, 5]
b = [1,2,3,4,5,6,7,8,9,10,11]


def insertShiftArray(lst, element):
    nums = (len(lst) + 1) // 2
    new_arr = lst[0:nums:]
    new_arr.append(element)
    new_arr.extend(lst[nums::])
    return new_arr
