# Программа запрашивает список целых чисел, а затем вычисляет по нему следующие значения:
# - count:   количество введенных чисел (длину списка)
# - sum:     сумму чисел
# - lowest:  минимальное число
# - highest: максимальное число
# - mean:    среднее значение
# - median:  медиану
# Определение. Медианой ряда чисел называется число, стоящее посередине упорядоченного по возрастанию ряда чисел 
# (в случае, если количество чисел нечётное). Если же количество чисел в ряду чётно, то медианой ряда является 
# полусумма двух стоящих посередине чисел упорядоченного по возрастанию ряда.

sum = 0
lowest = None
highest = None
numbers = []
while True:
    try:
        line = input("Input a numer or Enter to finish: ")
        if not line:
            break
        number = int(line)
        numbers.append(number);
        sum += number
        if lowest is None or number < lowest:
            lowest = number
        if highest is None or number > highest:
            highest = number
    except ValueError as err:
        print(err)
print("Numbers:", numbers)

if numbers:   # список чисел не пуст 
    #
    # Недостающий код напишите здесь и замените "XXX" в последующем print() нужными выражениями
    #
    print('count =', "XXX", "sum =", sum, "lowest =", lowest,
          "highest =", highest, "mean =", "XXX",
          "median =", "XXX"
         )

input("\nPress enter to exit")
