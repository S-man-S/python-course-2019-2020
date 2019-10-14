# python-course-2019-2020
Курс "Программирование на Python" для студентов школы программирования

# Lesson01 - Знакомство
Общее описание деятельности программиста. Классификация языков программирования. Характеристики Python. Знакомство со средой программирования IDLE. Программа приветствия пользователя и её доработка для запроса возраста и вывода, через сколько лет человеку исполнится 40. Разбор возможных ошибок этой программы.
Системы контроля версий. Основы работы с Git.

# Lesson02 - Ошибки. Исключения. Переменные. Модули. Операции. Типы данных
Типы ошибок программирования. Понятие исключений. Разбор работающей программы с логической ошибкой. Выявление и классификация этой ошибки.
Ссылочная модель переменных в Python. Требования к именам переменных. Импорт модулей. Модуль математических операций math. Операторы. Основные типы данных (int, float, bool, str). Модуль для генерации случайных чисел random с демонстрацией вариантов его использования. Проблема точности float и как её избежать. Практическое задание «Стоимость 2-ух товаров» и домашнее задание «Электронные часы»

# Lesson03 - Модель памяти. Управляющие конструкции IF и WHILE
Понятия пространства имён (namespace) и пространства объектов (heap). Как работает оператор присваивания в Python. Цепочечное и множественное присваивания, а также присваивание, совмещённое с арифметической операцией. Константы. Неизменяемость простых типов данных. Условный оператор if. Варианты ветвлений. Тернарный оператор выбора. Практическое задание c оператором if. Цикл while. Пример программы, использующей цикл while с ошибкой. Поиск и исправление этой ошибки. Бесконечный цикл. Его возможные последствия и варианты использования. Вложенный цикл. Практическое задание со вложенным циклом. Практические задачи на if и while – программы "Отгадай число" и "Задумай число" в классе и на дом

# Lesson04 - None. Is и is not. Списки. Цикл for
NoneType и None. Операторы is и is not. Пример использования None. Типы коллекций в Python. Определение последовательностей и пояснение принадлежности строк и списков к последовательностям. Варианты объявления списков. Популярные методы для работы со списками. Примеры скриптов, использующих эти методы. Доработка примера обработки списка чисел по предоставленному шаблону для определения количества элементов в списке, среднего значения и медианы. Изменяемые (mutable) и неизменяемые (immutable) последовательности. Отнесение списков и строк к нужной категории последовательностей с демонстрацией примера. Синтаксис цикла for. Функция range() для генерации числовой последовательности. Использование range() c циклом for. Примеры скриптов с циклом for. Практическое задание на решение с циклом while и for, их сравнение. Задания на переделывание готового скрипта с циклом while на использование цикла for. Пример программы «Ужасная поэзия». Развитие этого примера на использование параметра командной строки. Домашнее задание на развитие «Ужасной поэзии» для отсеивания дублированных строк в строфе и загрузку существительных и глаголов из файлов

# Lesson05 – Кортежи. Потоки. Файлы. Форматирование строк
5 способов форматирования строк, практическое задание на использование str.format() и f-strings. Определение кортежа как ещё одного вида последовательности. Неизменяемость кортежей, синтаксис их объявления. Популярные методы для работы с кортежами. Пример на кортежи. Именованные кортежи collection.namedtuple и усовершенствованные именованные кортежи с использованием синтаксиса классов и аннотациями типов – typing.NamedTuple. Потоковый ввод-вывод. Потоки как файлы. Перенаправление потоков ввода-вывода. Пример на перенастройку ввода-вывода для написанной ранее программы на использование потоков. Файловые форматы. Работа с текстовыми файлами. Совместные практические занятия на различные варианты чтения текстовых файлов. Совместная реализация задания на копирование данных из одного текстового файла в другой. Домашние задания: 1) Развитие программы «Ужасная поэзия» до 3-ей версии с поддержкой прилагательных и структурированием кода (желательно самостоятельное применение учениками собственных функций) 2) Программа «Лев Толстой и копирайтер» с подсчетом статистик по текстовому файлу с романом «Война и мир»


# Lesson06 – Собственные функции. Пространства имён  
Необходимость собственных функций. Виды функций в Python. Синтаксис объявления функции. Документирование функции с помощью Doc String. Типичный состав Doc String. Передача параметров и возврат значений функции на примерах. Особенность значений по умолчанию в Python. Передача параметров по ссылке. Присваивание параметра в функции. Возврат мульти-значений из функции. Анонимные функции. Области видимости. Разделение пространства имён областями видимости. Перекрытие переменных в функциях. Стек исполнения функций с демонстрацией примера. Домашнее задание на разработку библиотеки функций. Домашнее задание «Гистограмма в файле» на разработку по заданному шаблону с использованием модулей и функций.
