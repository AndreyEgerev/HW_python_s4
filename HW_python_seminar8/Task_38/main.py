# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1 - добавление контакта
# 2 - вывод всех
# 3 - поиск по фамилии
# 4 - выход

import os
import interface
import workfile

def main(pathPhoneBook):
    flag = True
    exitList = ['x', 'exit', 'e', 'х', 'выход', '1']
    findList = ['f', 'find', 'п', 'поиск', '2']
    readList = ['r', 'read', 'в', 'вывод', '3']
    addList = ['a', 'add', 'д', 'добавить', '4']
    removeList = ['d', 'delete', 'у', 'удалить', '5']
    changeList = ['c', 'change', 'и', 'заменить', '6']

    while flag:
        interface.PrintMenu()
        userAction = input("Введите необходимое действие: ").lower()
        if userAction in exitList:      #Выход
            flag = False
            print("Пока")
        #Поиск записи
        elif userAction in findList:    
            findText = input("Введите имя, фамилию или номер телефона ").lower()
            print(workfile.FindRecord(findText, pathPhoneBook))
        #Вывод справочника
        elif userAction in readList:    
            book = workfile.ReadBook(pathPhoneBook)
            interface.PrintBook(book)
        #Добавление записи
        elif userAction in addList:     
            addRecord = interface.InputLine('')
            print(workfile.AddRecord(addRecord, pathPhoneBook))
        #Удаление записи
        elif userAction in removeList:  
            findText = input("Введите имя, фамилию или номер телефона ").lower()
            print(workfile.RemoveRecord(findText,pathPhoneBook))
        #Изменение записи
        elif userAction in changeList:  
            findText = input("Введите имя, фамилию или номер телефона изменяемого контакта ").lower()
            changeText = interface.InputLine('Введите новые данные')
            print(workfile.ChangeRecord(findText,changeText,pathPhoneBook))
        #В случае неправильного ввода
        else:
            print("Действие не распознано. Попробуй еще раз")


# путь к файлу справочнику
pathPhoneBook = os.getcwd() + '\HW_python_seminar8\Task_38\phonebook.txt'

main(pathPhoneBook)       
