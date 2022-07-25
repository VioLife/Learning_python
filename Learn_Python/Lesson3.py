#Задайте список из нескольких чисел. 
# #Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random
from functools import reduce
Lst = []

# Генерируем cписок из 5 чисел от 1 до 10 во влючении:
Lst = [random.randint(1,10) for i in range(5)]
print(Lst)
#Применяем функцию reduce:
sum_Lst = reduce(lambda x, y: x+y, Lst)
print(sum_Lst)

# Напишите программу, которая определит позицию второго 
#вхождения строки в списке либо сообщит, что её нет.
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3


#my_str = ["qwe", "asd", "zxc", "qwe", "ertqwe"]

f = lambda item: my_str.count(item) == 1
res =list(filter(f,my_str))
print(res)
sum_count = list(enumerate(res))
print(sum_count)
for e in sum_count:
   print(e[0])
   b = len(e) + 1
print(f'Количество слов в строке: {b}') #находит индексы слов подходящих и выводит их в отдельную строку

# Задайте список из вещественных чисел. 
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]
from functools import reduce

f = list(map(lambda x: x%1*100, my_list))

print(f)

smallest_num = min(f)
biggest_num = max(f)


print(f'Самое маленькое значение: {smallest_num}')
print(f'Самое большое значение: {biggest_num}')

res = biggest_num -smallest_num

print(f'Разница между наибольшим и наименьшим элементом списка: {res}')


#Вычислить число c заданной точностью d
#Пример:
# при d = 0.001, π = 3.141.   10^{-1} ≤ d ≤10^{-10}

d = float(input('Введите дробное число: '))

lst = [i for i in str(d)]

num = list(enumerate(lst))

print(num)

for e in num:
       print(e[-1], end = " ")
       
result = ' '.join(str(e) for e in num)

#count = 0
#c = []
#for i in result:
   # c.append(i)
    #count += 1
#print(c)
#print(count)
    
x = int(input('Введите число элементов до запятой: '))
import math
p = math.pi
print(p)

print(round(p,x))


#Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

def factors(n):
    return[x for x in range(2,n//2+1) if n%x == 0]
print(factors(63))


#Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
#Пример:
# => 2*x² + 4*x + 5 = 0

lst1 = ['x^2', '+x', '+', '=']
lst2 = ['2', '4', '5', '0']

res = list(zip(lst1,lst2))
print(res)

from random import randint
lst3 = [randint(0, 101) for i in range(4)]
print(lst3)

res2 = list(zip(lst1,lst3))
print(res2)


import functools

end = functools.reduce(lambda x,y: x+y, res2)
print(end)


result = ','.join(str(n) for n in end)
print(result)







    

        







