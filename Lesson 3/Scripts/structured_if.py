﻿# Выявление разницы между if-elif и последовательным if

grade_rus = 70   # выпускник набрал 70 баллов по русскому языку
grade_math = 80  # выпускник набрал 70 баллов по математике

# нужно вывести сколько выпускник набрал по каждому обязательному предмету,
# по которым он/она превышает минимальный проходной балл == 50

# неправильный вариант - выполняется только одна ветка условия
if grade_rus >= 50:
    print("Вы прошли по русскому языку со следующими баллами: ", grade_rus)
elif grade_math >= 50:
    print("Вы прошли по математике со следующими баллами: ", grade_math)

# правильный вариант - будет оцениваться каждый проходной балл
if grade_rus >= 50:
    print("\nВы прошли по русскому языку со следующими баллами: ", grade_rus)
if grade_math >= 50:
    print("Вы прошли по математике со следующими баллами: ", grade_math)

input("\nНажмите Enter для выхода")
