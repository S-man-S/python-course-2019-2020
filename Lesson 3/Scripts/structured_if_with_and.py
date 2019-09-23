﻿# Вложенные операторы if и объединение условий по and

precipitation = True   # признак высокой влажности, при истинном значении которого возможны осадки в виде дождя или снега
temperature = +8       # температура больше нуля означает, что при высокой влажности есть вероятность дождя
                       # а если температура меньше нуля, то скорее всего, при высокой влажности, пойдет снег

# выдаем рекомендации после анализа влажности и температуры воздуха
if precipitation:
    if temperature > 0:
        print("Не забудьте взять с собой зонтик")
    else:
        print("Нужно одеть зимние ботинки и пальтишко")

# сокращенный вариант, эквивалентный предыдущему блоку кода
if precipitation and temperature > 0:
    print("Не забудьте взять с собой зонтик")
elif precipitation:
    print("Нужно одеть зимние ботинки и пальтишко")

input("\nНажмите Enter для выхода")
