# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


num = int(input('Введите целое значение: '))
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print("Сумма цифр числа равна: ", sum)
        

# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def func (x):
    factorial = 1
    for i in range (1,x + 1):
         factorial = factorial * i
         print(factorial, end = ' ')
         
n = int(input('Введите любое значение: '))
func(n)

#Задача 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
#Пример:
#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


def Calculation(n,amount = 0):
    amount += (1 + 1/(n))**(n)
    return amount

n = int(input('Введите любое целое число:'))
spisok = range(n)
spList = ' '
sumSpisok = 0
for i in range ( 1, n + 1):
    sumSpisok += Calculation(i)
    spList += ' ' + str(Calculation(i))
print(f"Cумма последовательности чисел {spList} = {sumSpisok}")

#Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов 
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

#Реализуйте алгоритм перемешивания списка.

n = int(input('Введите любое целое число:'))
my_list = []
import random


for i in range(-n,n+1):
     
    my_list.append(i)
print(my_list)

random.shuffle(my_list)
print(my_list)


def multiply(n):
    total = -n
    for i in range(-n, n+1):
        total *= i       
    print(f"Произведение чисел в списке равно {total}")
multiply(4)

print("\n".join(map(str,my_list)))

##Дополнительный вариант хранения в txt в форме списка
#with open("file.txt", "w") as f:
   # for s in my_list:
     #   f.write(str(s) +"\n")

#with open("file.txt", "r") as f:
  #for line in f:
    #my_list.append(int(line.strip()))
