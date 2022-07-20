#Задача1. Вычислить число c заданной точностью d
#Пример:
# при d = 0.001, π = 3.141.   10^{-1} ≤ d ≤10^{-10}

d = float(input('Введите дробное число: '))

s = str(d) # перевела в строковый формат дробное число
k = abs(s.find('.') - len(s)) - 1 #вычислила количество цифр перед запятой
print(abs(s.find('.') - len(s)) - 1)

import math # нашла значение пи из библиотеки
p = math.pi
print(p)

d_new = p%1 #устранила целую часть в значени пи
print(d_new)

print(round(d_new,k)) #c помощью готовой функции вывела значение с нужным количеством знаков

#print('%.4f' % d)


#Задача2.Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите любое целое число: '))

list_multiplier = []
simple = 2
while n > 1:
    if n % simple == 0:
        list_multiplier.append(simple)
        n = n/simple
    else:
        simple += 1
print(list_multiplier)

#Задача3. Задайте последовательность чисел.
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

my_list = []

for i in range(7):
    num = int(input('--> '))
    my_list.append(num)
print(my_list)

unique_array = list(set(my_list))
print(unique_array)


#my_list = [1, 6, 4, 3, 2, 4, 6, 8, 3] --> примерный список хаотичной последовательности

#Задача4. Задана натуральная степень k. 
#Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
#Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

path = '/Users/mac/Desktop/Python_Homework/Learn_Python/file.txt'

with open(path, 'r') as change_file:
    formula =change_file.read()
    
formula1 = formula.split()
print(formula1)
formula2 = formula1[:-2]
print(formula2)
formula3 = [int(formula2[0][:-3]), int((formula2[1]+formula2[2])[:-1]), int(formula2[3]+formula2[4])]
print(formula3)

from random import randint
new_formula = [randint(0, 101) for i in range(3)]
print(new_formula)


for i in range(len(new_formula)):
    new_formula[i] = str(new_formula[i])
    a = new_formula[0]
    b = new_formula[1]
    c = new_formula[2]
print(new_formula)
    

formula4 = [(a + formula1[0][1:4]), formula1[1], b + formula1[2][-1], formula1[3], c, '=', ' 0']


print(formula4)

path_res = '/Users/mac/Desktop/Python_Homework/Learn_Python/file2.txt'

with open(path_res,'w') as res_file:
    res_file.write('Уравнение с рандомными коэффициентами:' + str(formula4))



