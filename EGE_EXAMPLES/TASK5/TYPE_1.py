#Посимвольное двоичное преобразование
#В коде указаны строки, которые обязательно должны присутствовать в коде

for N in range(0, 1000): #Читайте условие, какое число входит в цикл
    s = bin(N)[2:]
    #Здесь в сухую прописываем алгоритм с действиями,
    #которые воспроизводятся над числом
    R = int(s, 2)
    if R > 'добавляем число и знак по условию':
        print(R)
        break
