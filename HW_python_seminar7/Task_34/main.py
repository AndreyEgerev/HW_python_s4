# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам 
# да-да-да не-беда

# функция определения количества гласных в фразе
def countVowels(songString):
    vovelLetter = 'ауоыиеёэюя' #а, у, о, ы, и, э, я, ю, ё, е
    return len(list(filter(lambda letter: letter in vovelLetter, songString)))

# функция определения ритма кричалки
def NormSongVinny(song):
    rhythms = set(map(countVowels, song))

    # вариант решения без использования map и filter      
    # vovelLetter = 'ауоыиеёэюя'
    # songString = 0
    # rhythms = {}
    # for i in range(len(song)):
    #     for j in range(len(song[i])):
    #         if song[i][j] in vovelLetter:
    #             songString += 1
    #     rhythms.add(songString)
    #     songString = 0
    # nBukc = "Парам пам-пам"

    if len(rhythms) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"
    
# Приветствие
print("Определение ритма кричалок Винни-пуха")
#poem = 'да-да-да да-да-да'
poem = input("Введите строки стихотворения - ").lower().split(" ")
#print(*poem)
print(NormSongVinny(poem))
