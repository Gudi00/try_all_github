import random

mas = [random.randint(1, 10) for i in range(8)]
print(mas)
print()

def summa(*numbers):
    rez = 0
    for value in numbers:
        print(value)

summa(*mas)

# def solution(arr):
#     print(arr)
#     for i in range(1, len(arr)):
#         for j in range(1, len(arr) - i):
#             if arr[j-1] > arr[j]:
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#
#     print(arr)
#
# solution(mas)
# print(mas)
