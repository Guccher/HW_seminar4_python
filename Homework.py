# Task № 1 
# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

# from math import pi

# d =  int(input("enter the number with the specified accuracy d:\n"))
# print(f'the number of pi with a given precision {d} = {round(pi, d)}')


# Task № 2
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# n = int(input("Enter number: "))
# i = 2 
# multipliers_list = []
# old = n
# while i <= n:
#     if n % i == 0:
#         multipliers_list.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(f"Prime factors of a number {old} given in the list: {multipliers_list}")


# Task № 3
#  Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# elements_list = list(map(int, input("Enter the numbers separated by a space:\n").split()))
# print(f"Source list: {elements_list}")
# new_list = []
# [new_list.append(i) for i in elements_list if i not in new_list]
# print(f"A list of non-repeating elements: {new_list}")


# Task № 4
#  Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.    
#     *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x²

# from random import randint
# import itertools

# k = randint(2, 7)

# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10) 
#     return ratios

# def get_expression(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     expression = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in expression:
#         x.append(' + ')
#     expression = list(itertools.chain(*expression))
#     expression[-1] = ' = 0'
#     return "".join(map(str, expression)).replace(' 1*x',' x')


# ratios = get_ratios(k)
# expression1 = get_expression(k, ratios)
# print(expression1)

# with open('expression.txt', 'w') as data:
#     data.write(expression1)


# # Task № 5
# # Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.



# k = randint(2, 5)

# ratios = get_ratios(k) 
# expression2 = get_expression(k, ratios)
# print(expression2)

# with open('33_Polynomial2.txt', 'w') as data:
#     data.write(expression2)




