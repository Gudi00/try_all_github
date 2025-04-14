mas = [9, 3, 1, 5, 6, 7, 1]

def vst():

    l = len(mas)
    for n in range(0, l):
        index = n
        for i in range(n, l):
            if mas[index] > mas[i]:
                index = i
        temp = mas[n]
        mas[n] = mas[index]
        mas[index] = temp
    print(mas)

print(vst())