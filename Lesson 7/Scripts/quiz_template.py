# Викторина по выбору правильного варианта ответа
# Программа проверяет знания пользователя, задавая ему вопросы и предлагая на выбор ответ из нескольких вариантов
# Блоки информации с темой, вопросом, вариантами ответов, правильным ответом и пояснениями читаются из текстового файла.
# Строки данных в текстовом файлы следуют одна за другой без пропусков
# Структура текстового файла, с которым работает программа:
# 1-я строка содержит название викторины, а далее следуют блоки информации  по следующей схеме:
# <тема вопроса>
# <вопрос>
# <ответ 1>
# <ответ 2>
# ...
# <ответ N>, N не превышает 9
# <порядковый номер правильного варианта ответа>
# <пояснения к выбору правильного варианта ответа>
# Все компоненты в блоке информации по вопросу располагаются каждая на отдельной строке.
# При этом символ "/" внутри строки означает, что при отображении строки в программе в этом месте нужно вставить перевод строки

import sys

class MyRangeError(Exception): pass

def get_integer(message, name="целое число", minimum=None, maximum=None):
    """ (str, str, int, int) -> int
    Запрашивает у пользователя целочисленное значение name с приглашением message и возвращает это значение.
    Контролирует, чтобы введенное значение было строго больше minimum и строго меньше maximum, если эти параметры заданы
    """
    message += ": "
    while True:
        try:
            line = input(message)
            int_val = int(line)
            if (minimum is not None and minimum > int_val) or (maximum is not None and maximum < int_val):
                raise MyRangeError("Ожидается значение {0} между {1} и {2} ".format(name.upper(), minimum, maximum))
            return int_val
        except MyRangeError as err:
            print("ОШИБКА.", err)
        except ValueError as err:
            print("ОШИБКА. Значение {0} должно быть целочисленным".format(name.upper()))

def open_file(file_name, mode):
    """ (str, str) -> opened file
    Открывает файл file_name в режиме mode и возвращает файловую переменную, указывающую на этот файл
    Предусловие: файл file_name должен быть доступен на открытие в заданном режиме mode, иначе программа завершает свою работу
    """
    try:
        the_file = open(file_name, mode, encoding="cp1251")
    except IOError as err:
        print("Невозможно открыть файл", file_name, "Работа программы будет завершена.\n", err)
        input("\n\nДля выхода нажмите Enter.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """ (opened_file) -> str
    Возвращает очередную строку из файла. Символ "/" в строке заменяется на "\n", конечные пробельные символы отбрасываются
    """
    pass
    return ""

def next_block(the_file):
    """ (opened_file) -> tuple
    Возвращает очередной блок данных, касающийся одного вопроса викторины, из открытого файла the_file
    Значение возвращается в кортеже следующей структуры: (str topic, str question, list of str answers[], int correct, str explanation)
    Если при чтении элементов блока достигнут конец файла или пустая строка,
    то все элементы данного кортежа содержат None
    """
    pass
    return None, None, None, None, None

def welcome(title):
    """Приветствует пользователя и сообщает ему название викторины."""
    print("\t\tДобро пожаловать в Викторину!\n")
    print("\t", title, "\n")
 
def main():
    # открыть файл, считать название викторины из 1-ой строки файла и поприветсововать пользователя
    quiz_file = open_file("py_struct.txt", "r")
    title = next_line(quiz_file)
    welcome(title)
    # инициализировать счетчки количества заданных вопросов и правильных ответов на них
    total = score = 0

    # извлечение из файла первого блока <тема, вопрос, ответы, верный вариант, пояснения>
    topic, question, answers, correct, explanation = next_block(quiz_file)
    while topic is not None:
        # вывод вопроса на экран
        pass

        # получение ответа
        answer_num = get_integer("Ваш ответ", "ответ", 1, len(answers))

        # проверка ответа
        pass

        # вывод пояснений и текущего счета

        # приращение счетчика заданных вопросов
        total += 1

        # получение следующего блока из файла
        topic, question, answers, correct, explanation = next_block(quiz_file)

    quiz_file.close()

    print("Это был последний вопрос!")
    print("Правильных ответов {0} из {1}".format(score,total))
 
main()  
input("\n\nДля выхода нажмите Enter.")
