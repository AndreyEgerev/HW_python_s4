# Модуль работы с пользователем

# Функция вывода меню
def PrintMenu():
    print("Телефонный справочник")
    print("Доступные действия: \n 1. e - eXit \t\tвыХод \n 2. f - Find contact \tПоиск контакта \n 3. r - Read all \tВывод всех контактов \n 4. a - Add contact \tДобавить контакт \n 5. d - Delete contact \tУдалить контакт \n 6. c - Change contact \t Изменить контакт")

# Функция ввода данных записи
def InputLine(text):
    if len(text)>0:
        print(text)
    resultStr = input('Введите Фамилию ').lower()
    resultStr = resultStr + ':' + input('Введите Имя: ').lower()
    resultStr = resultStr + ':' + input('Введите Отчество: ').lower()
    resultStr = resultStr + ':' + input('Введите Номер телефона: ').lower() + '\n'
    return resultStr

# Функция вывода в консоль данных
def PrintBook(book):
    for i in range(len(book)):
        print(book[i].title().replace(':', ' '), end='')


    