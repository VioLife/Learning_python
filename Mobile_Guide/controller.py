from init import input_data
from view import phone_view
from data import get_phone
from data import get_info
from data import get_info1
from logger import phone_number
#from imp import import_data
import Storage
import pandas as pd




def ring_me_now():
    
    
    a = get_phone(input_data('Введите номер телефона:')) #Запрашиваем у пользователя номер телефона
    b = get_info(input_data('Введите имя:')) #Запрашиваем у пользователя имя абонента
    c = get_info1(input_data('Введите город:')) #Запрашиваем у пользователя город проживания
    
    w = input('Введите имя запрашиваемого абонента: ') #Запрашиваем имя на ранее введенные данные, если уже такое имя есть, то уточняем продублировать ли данные
    
    
    st = str(f'Абонент с именем {b} из города {c} внесен(a) в телефонную книгу с  номером телефона {a}') #красиво выводим данные, запрошенные у пользователя
    print(st)
    phone_number(st) #залоггировали данные, то есть каждая строка последовательно вносится в файл csv и там сохраняется и накапливается
  

    phone_view(a,b,c) #отображение в интерфейсе
    
    res = {b: a}
    for key in res:
        if b == w:
            print(f'Вы хотите продублировать запись? Aбонент с именем {b} уже записан с номером телефонa {a}')
        else:
            print('Такого абонента нет в телефонном справочнике')
          
            
    
    res1 = Storage.save_info(a,b,c) #вывод полученных данных через словарь в табличной форме (применяем модуль с пакетом)
    
    print(res1)
    
    
    
    
    path = '/Users/mac/Desktop/Python_Homework/log.csv' #считать все данные сохраненные в csv 
    df = pd.read_csv(path)
    #print(df)
   
    
    text = str(df) #и сохраняем их в переменную в строковом виде
            
    path2 = '/Users/mac/Desktop/Python_Homework/Mobile_Guide/end.txt'
 
    with open(path2, 'w') as f: #переносим наши данные в новый текстовый файл end.txt
        f.write(text)
    
    
    return res1 


   



    

    

    


    

    

   
    

