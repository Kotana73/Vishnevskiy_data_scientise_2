# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

my_list = [True, 265, 17.1, (3.14 + 2j), 'super Duper', [5, 8], (9, 16, 7.3), {50, None, False, 'jgf'},
           range(5), bytearray(b'text')]
for el, p_class in enumerate(my_list, 0):
    print(el, '-', p_class, ' - ', type(p_class))
