#Все 5-буквенные слова, составленные из букв Л, Н, Р, Т,
# записаны в алфавитном порядке. Вот начало списка:
# 1 ЛЛЛЛЛ
# 2 ЛЛЛЛН
# 3 ЛЛЛЛР
# 4 ЛЛЛЛТ
# 5 ЛЛЛНЛ
# Запишите слово, которое стоит на 150-м месте
# от начала списка.

a = {0: "Л", 1: "Н", 2: "Р", 3: "Т"}
k = 0

for a1 in range(0, len(a)):
    for a2 in range(0, len(a)):
        for a3 in range(0, len(a)):
            for a4 in range(0, len(a)):
                for a5 in range(0, len(a)):
                    k += 1

                    if k == 150:
                        print(a[a1], a[a2], a[a3], a[a4], a[a5])