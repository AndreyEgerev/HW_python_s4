# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

def CreateArray(n):
    numbers = []
    for i in range(n):
        numbers.append(int(input(f"Введите {i+1}-й элемент: ")))
    return numbers

def SortArray (numbers, rangeNum):
    indexNumbers =[]
    for i in range(len(numbers)):
        if numbers[i] >= min(rangeNum) and numbers[i] <= max(rangeNum):
            indexNumbers.append(i)
    return indexNumbers

n = int(input("Введите кол-во элементов первого множества: "))
numbers1 = CreateArray(n)
print(numbers1)

print("Введите диапазон отбора: ")
rangeNumber = CreateArray(2)
print(rangeNumber)

print("Индексы элементов входящих в заданый диапазон: ")
print(SortArray(numbers1, rangeNumber))