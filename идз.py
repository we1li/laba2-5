print("Введите числа")
a = tuple(map(int, input().split()))
for i, x in enumerate(a):
    if a[i] != a[-1]:
        if a[i] >= a[i+1]:
            print("Номер элемента нарушающего упорядоченность", i+1)
            break
    else:
        print("Кортеж упородочен по возрастанию")