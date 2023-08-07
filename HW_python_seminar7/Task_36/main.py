# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: Вывод:
# print_operation_table(lambda x, y: x * y) 
#  1    2   3   4 5 6
#  2    4   6   8 10 12
#  3    6   9   12 15 18
#  4    8   12  16 20 24
#  5    10  15  20 25 30
#  6    12  18  24 30 36 

# функция вычисления значений выражения и вывода в консоль 
def print_operation_table(operation, num_rows=6,num_columns = 6):
    rows = list(range(1, num_rows+1))
    columns = list(range(1, num_columns+1))
    rezaltArray = list(map(lambda i: list(map(lambda j: operation(i, j), columns)), rows))

    for row in rezaltArray:
        print(*row, sep='\t')


# Приветствие
print("Программа вычисления значений")
# Ввод количества строк, столбцов
nRows = int(input("Введите количество строк - "))
nColumns = int(input("Введите количество столбцов - "))
operation = lambda x,y: x*y

print_operation_table(operation, nRows, nColumns)
#print_operation_table(lambda x,y: x+y)