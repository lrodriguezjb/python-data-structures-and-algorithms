a = [1, 2, 3, 4, 5, 6]


def ArrayReverse(arr):
    output = []
    size = len(arr)
    for i in range(0, size):
        data = arr[size-(i+1)]
        output.append(data)
    return output


answer = ArrayReverse(a)

print(answer)
