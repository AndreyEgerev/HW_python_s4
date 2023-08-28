# Модуль работы с файлом

# Функция вывода всего телефонного справочника
def ReadBook(path):
    with open(path, 'r', encoding='utf-8') as file:
        book = file.readlines()
    return book

# Функция изменения записи в телефонном справочнике
def ChangeRecord(oldRecord, changeRecord,path):
    flag = False
    newBook = list()
    with open(path, 'r', encoding='utf-8') as file:
        records = file.readlines()
    for record in records:
        if oldRecord in record:
            oldRecord = record
            record = record.replace(oldRecord,changeRecord)
            flag = True
        newBook.append(record)
    if flag:
        with open(path,'w', encoding='utf-8') as file:
            file.writelines(newBook)
        return 'Запись изменена'
    else: return 'Запись не найдена'
  
# Функция удаления записи в телефонном справочнике
def RemoveRecord(record, path):
    with open(path, 'r', encoding='utf-8') as file:
        records = file.readlines()
    removeRecord = [line for line in records if record not in line]
    if len(removeRecord) < len(records):
        resultStr = f'Запись удалена. Удалено записей - {len(records)-len(removeRecord)}'
        with open(path, 'w', encoding='utf-8') as file:
            file.writelines(removeRecord)
    else: resultStr = 'Запись не найдена'
    return resultStr
    
# Функция поиска записи в телевонном справочнике
def FindRecord(findText, path):
    file = open(path, 'r', encoding='utf-8')
    flag = True
    for record in file:# & flag == True:
        if findText in record:
            resultStr = record
            flag = False
            break
    else:
        resultStr = 'Искомого элемента нет' 
    file.close()
    if flag: return resultStr
    else: return resultStr[:-1].title().replace(':', ' ')

# Функция добавления записи в телефонный справочник
def AddRecord(record, path):
    file = open(path, 'a', encoding='utf-8')
    file.writelines(record)
    file.close()
    return 'Данные добавлены'
