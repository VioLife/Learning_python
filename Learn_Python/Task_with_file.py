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
    
        
