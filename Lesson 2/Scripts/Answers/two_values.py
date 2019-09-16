val_1 = input("Введите первое значение: ")
val_2 = input("Введите второе значение: ")

try:
    result = int(val_1) + int(val_2)
except ValueError:
    result = str(val_1) + str(val_2)

print("Полученный результат: ", result)

input("\n\nНажмите Enter для выхода")
