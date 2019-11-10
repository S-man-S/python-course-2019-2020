﻿# Исходный список
a_list = [1, 30, "text", True, 30 , 100 , False]
# Отображаем содержимое списка
print( "Список a_list:", a_list)
# На основе списка создается множество
a_set = set(a_list)
# Отображаем содержимое множества
print("Множество a_set:", a_set)
# Создаем еще одно множество
b_set = {1, 30, "text", True, 30, 100, False}
# Отображаем содержимое 2-го множества
print("Множество b_set:", b_set)
# Проверяем равенство множеств
print("Равенство множеств:", a_set==b_set)
# Вхождение элемента 1 в множество
print("Элемент 1 в множестве a_set:", 1 in a_set)
# Вхождение элемента True в множество
print("Элемент True в множестве b_set:", True in b_set)

input("\n\nДля выхода нажмите Enter.")
