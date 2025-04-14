mas = [1, 3, 4, 5, 6, 7, 8]

def binary(n):
    left = 0
    right = len(mas) - 1
    while right > left:
        temp = (right + left) // 2
        mid = mas[temp]
        if n > mid:
            left = temp + 1
        else:
            right = temp
    if n == mas[left]:
        return left+1
    return -1

print(binary(8))