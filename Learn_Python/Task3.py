#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
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

#Задача4.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов 
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

#Реализуйте алгоритм перемешивания списка.
    
  






    


   
    
    
    

 


  
  
  
  
    # num = int(input('--> '))
    # my_list = []
    
    # factorial = 1
    #     if num < 0:
    #         print("Факториал не вычисляется для отрицательных чисел")
    #     elif num == 1:
    #         return num
    #     else:
    #         for i in range (1, num+1):
    #             my_list.append(num)
    #             factorial = factorial * i(my_list)
    #                 print(f"произведение чисел от 1 до N: {factorial}")