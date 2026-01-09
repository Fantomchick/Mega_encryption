itog = ''
alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ123456789,.!?-'
smeshenie = 5   #Создаем переменную с шагом шифровки
message = input("Сообщение для шифровки: ").upper()    #создаем переменнную, куда запишем наше сообщение

for i in message:
    mesto = alfavit.find(i)
    new_mesto = mesto + smeshenie
    if i in alfavit:
        itog += alfavit[new_mesto]  # Задаем значения в итог
    else:
        itog += i

for i in message:
    mesto = alfavit.find(i)
    new_mesto = mesto - smeshenie
    if i in alfavit:
        itog += alfavit[new_mesto]  # Задаем значения в итог
    else:
        itog += i
print(itog)        