# Компьютерный датчик настроения
# Демонстрирует использование elif и ветки else на случай, если "что-то пошло не так"

import random

print("Я ощущаю вашу энергетику. От моего процессора не скрыть ваши чувства.")
print("Итак, ваше настроение...")

mood = random.randint(1, 3)

if mood == 1:
    # радостное
    print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | .     . |
       |  `...`  |
       -----------
                   """)
elif mood == 2:
    # нейтральное  
    print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | ------  |
       |         |
       -----------
                   """)
elif mood == 3:
    # скверное
    print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       |  .'.    |
       | '   '   |
       -----------
                   """)
else:
    print("Не бывает такого настроения! (Должно быть, вы совершенно не в себе).")

print("... Но это только сегодня. ... А завтра может всё измениться ...")

input("\nНажмите Enter для выхода.")
