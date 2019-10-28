﻿# Создаем словарь
syms = dict ( [("a", "первый"), ("b", "второй")] )
# Содержимое 1-го словаря
print("Cлoвapь syms:", syms)

# Создаем еще один словарь
more_syms = dict ( [("c", "третий"), ("d", "четвертый"), ("b", "еще более второй")] )
# Содержимое 2-го словаря
print("Cлoвapь more_syms:", more_syms)

# Добавляем второй словарь в первый
syms.update(more_syms)

# Содержимое объединенного словаря
print("Cлoвapь syms после объединения:", syms)
# Длина словаря
print("Количество ключей в cлoвape :", len(syms))

# Доступ к элементу по ключу (ключ в словаре есть)
print("Элемент с ключом 'c' содержит значение:",
      syms.get ("c" , "нет такого ключа!"))

# Проверяем наличие ключа в словаре
print("Наличие элемента с ключом 'c':", "c" in syms)

# Удаляем элемент из словаря
del syms["c"]

# Содержимое словаря
print("Словарь syms после удаления ключа 'c':", syms)

# Доступ к элементу по ключу (ключа в словаре нет )
print("Элемент с ключом 'c' содержит значение:",
      syms.get ("c" , "нeт такого ключа!"))

# Проверяем наличие ключа в словаре
print("Наличие элемента с ключом 'с' :", "с" in syms)

# Список ключей словаря
print("Ключи cлoвapя :", list(syms.keys()))

# Список значений элементов словаря
print("Значения элементов cлoвapя :", list(syms.values()))

# Содержимое словаря
print("Содержимое cлoвapя :", list(syms.items()))

# Удаление элемента из словаря
print("Удаляется элемент со значением: ", syms.pop("b"))

# Содержимое словаря
print("Cлoвapь syms еще что-то содержит:", syms)

# Очистка словаря
syms.clear()

# Содержимое словаря
print("Cлoвapь syms пустой:", syms)

input("\n\nДля выхода нажмите Enter.")
