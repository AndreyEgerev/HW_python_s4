# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

def CreateArray(n):
    numbers1 = []
    for i in range(n):
        numbers1.append(int(input(f"Введите {i+1}-й элемент: ")))
    return numbers1

def SortArray (numbers, rangeNum):
    indexNumbers =[]
    for i in range(len(numbers1)-1):
        if numbers1[i] >= rangeNum[0] and numbers1[i] <= rangeNum[1]:
            indexNumbers.append(numbers1[i])
    return indexNumbers


n = int(input("Введите кол-во элементов первого множества: "))

numbers1 = CreateArray(n)
print(numbers1)
print("Введите диапазон отбора: ")
rangeNumber = CreateArray(2)
print(rangeNumber)
print(SortArray(numbers1, rangeNumber))