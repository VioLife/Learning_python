#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов 
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
    
    



        