import random
def quick_sort(arr):
    temp = [0, len(arr)-1]

    while temp:
        right = temp.pop()
        left = temp.pop()

        if left < right:
            wl, wr = left, right#fdsgdgdh
            mid = arr[(left + right) // 2]#z nkjflsadfdkasflkjslkdfjkhs
            while left <= right:
                while arr[left] < mid: left += 1
                while arr[right] > mid: right -= 1
                if left <= right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1

            if wr - left > right - wl:
                temp.extend([left, wr, wl, right])
            else:
                temp.extend([wl, right, left, wr])


mas = [random.randint(1, 10) for i in range(8)]
# mas = [3, 9, 6, 9]
print(mas)
def say2():
    print(mas)
quick_sort(mas)
print(mas)




