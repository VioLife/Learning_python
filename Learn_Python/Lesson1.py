#Задача1. Задайте список из нескольких чисел. 
# #Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = [2, 3, 5, 9, 3]
sum1 = 0
sum2 = 0
for i in range(len(my_list)):
    if my_list[0]%2 != 0 and my_list[-1]%2 !=0:
        sum1 = my_list[0] + my_list[-1]
    elif my_list[1]%2 != 0 and my_list[-2]%2 !=0:
        sum2 = my_list[1] + my_list[-2]
    else: 0
    
print(sum1)
print(sum2)

#Задача2. Напишите программу, которая найдёт произведение пар чисел списка.
# #Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]

my_list = []

for i in range(5):
    x = int(input('-->'))
    my_list.append(x)

print(my_list)

for i in range(len(my_list)):
    a = my_list[0]*my_list[-1]
    b = my_list[1]*my_list[-2]
    d = my_list[2]**2
    
print(a)
print(b)
print(d)

list_c = [a, b, d]
print(list_c)

#Задача3.Задайте список из вещественных чисел. 
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]


maxx = 0
minn = 0
res = 0

maxx = my_list[0]
for i in range(len(my_list)):
    my_list[i] = float(my_list[i])
    my_list[i] = int((my_list[i]%1)*100)
   
    print(my_list[i])
    while i < len(my_list):
        if my_list[i] > maxx:
            maxx = my_list[i]
        elif my_list[i] < maxx:
            minn = my_list[i]
        i += 1
    res = maxx - minn
    
        
print(f'Максимальная дробная часть: {maxx} Минимальная дробная часть: {minn}')
print(f'Разница между максимальной и минимальной дробной частью: {res}')

#Задача4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = int(input('Введите любое значение: ' ))
 
numerals = []

while num != 0:
    numerals.append(num%2)
    num //=2
 
print(numerals)

#Задача5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, -2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 



def fibonachi_plus(fib_n : int) -> list:
   
    fib_array = [0,1]
    if fib_n > 1:
        for i in range(2,fib_n+1):
            fib_array.append(fib_array[i-1]+fib_array[i-2])
    return fib_array

def fibonachi_minus(fib_n : int) -> list: 
    fib_array = [0,1]
    if fib_n > 1:
        for i in range(2,fib_n+1):
            fib_array.append(fib_array[i-2]-fib_array[i-1])
    return fib_array

def Result_Fib(fib_n : int) -> list:
    
    fib_plus = fibonachi_plus(fib_n) 
    fib_array = fibonachi_minus(fib_n) 
    fib_array = fib_array[::-1]
    for i in range(1,fib_n+1): 
        fib_array.append(fib_plus[i])
    return fib_array
        
fib_n = int(input("Введите номер числа Фибоначчи: "))
fib_list = Result_Fib(fib_n)
print(f"Для числа Фибоначчи = {fib_n} последовательность чисел будет равна : {fib_list}")
