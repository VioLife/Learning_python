#Создайте программу для игры в ""Крестики-нолики"".

print("*" * 5, " Игра Крестики-нолики для двух игроков ", "*" * 5)

field = list(range(1,10))

def draw_board(field):
   print("-" * 13)
   for i in range(3):
      print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
      print("-" * 13)

def take_input(player_move):
   value = False
   while not value:
      player_answer = input("Куда поставим " + player_move+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Повторите попытку ввода числа")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(field[player_answer-1]) not in "XO"):
            field[player_answer-1] = player_move
            value = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(field):
   win_position = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_position:
       if field[each[0]] == field[each[1]] == field[each[2]]:
          return field[each[0]]
   return False

def main(field):
    counter = 0
    win = False
    while not win:
        draw_board(field)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(field)
           if tmp:
              print(tmp, "Ура! Вы победитель!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(field)
main(field)

input("Нажмите Enter для выхода!")


#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""

def start():
    print(f'############# Игра "2021 конфета" ###############')
    print(f'Всего на столе лежит 2021 конфета')
    print(f'Каждый игрок по очереди берет не более чем 28 конфет')
    print(f'Выигрывает тот, кто заберет последние конфеты со стола!')
    print(f'######################################################\n')
    
import random
start()

gamer_1, gamer_2 = input('Введите имя 1 игрока: '), input('Введите имя 2 игрока: ')

n = input('Жеребьевка на право хода игрока - Enter')
n = random.randint(1, 2)
if n.isdigit():
    n = int(n)
    if n == 1:
        print(f'Первым будет ходить первый игрок: {gamer_1}!')
    else:
        print(f'Первым будет ходить второй игрок: {gamer_2}!')
    
#if n == 1:
    #print(f'Первым будет ходить первый игрок: {gamer_1}!')
#else:
   # print(f'Первым будет ходить второй игрок: {computer}!')

#def ID_game(matches): 
    #number_to_delete = matches % 4
    #if number_to_delete == 0:
       # n = random.randint(1, 29)
    #return n


matches =  int(input('Количество конфет на столе - внесите вручную {2021}'))
count = 1

current_gamer = gamer_1
#ID_game()
while matches > 0:
    print('Количество оставшихся конфет: {}'.format(matches))
    print(f'\n******** Ход номер: {count} ********')
    while True:
        number_to_delete = int(input('ход игрока {} (1-28): '.format(current_gamer)))
        if number_to_delete >= 1 and number_to_delete <= 28:
            matches = matches - number_to_delete 
        else:
            print("Некорректный ввод. Введите число от 1 до 28")
        break
    
    current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
    count += 1
    
    #current_gamer = computer if current_gamer == gamer_1 else gamer_1

print('Победил {}'.format(current_gamer))

#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.

path = '/Users/mac/Desktop/Python_Homework/Learn_Python/save.txt'

with open(path, 'r') as change_file:
    numerals = change_file.read()
    print(numerals)


def encode(numerals):
    encoding = ' '
    num = ' '
    count = 1

    if not numerals: return ' '

    for char in numerals:
        if char != num:
            if num:
                encoding += str(count) + num
            count = 1
            num = char
        else:
            count += 1
    else:
        encoding += str(count) + num
        return encoding
print(encode(numerals))

path_res = '/Users/mac/Desktop/Python_Homework/Learn_Python/save2.txt'

with open(path_res,'w') as res_file:
    res_file.write('Сжатие данных числовой строки представлено в таком виде:' + str(encode(numerals)))

def decode(numerals):
    decode = ' '
    count = ' '
    for char in numerals:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ' '
    return decode
print(numerals)