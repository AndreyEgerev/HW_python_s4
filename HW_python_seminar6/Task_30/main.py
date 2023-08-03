# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def CreateProgressiv (a1, d, n):
    progressiv = []
    for i in range(1,n+1):
        nI = a1 + (i-1)*d
        progressiv.append(nI)
    return progressiv


number1 = int(input("Введите 1-й элемент прогрессии: "))
d = int(input("Введите разность прогрессии   : "))
nItem = int(input("Введите кол-во элементов прогрессии: "))

numbers1 = CreateProgressiv(number1, d, nItem)
print(numbers1)
