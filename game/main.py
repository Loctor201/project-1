from data import *
from func import *
cm=0
while True:
    action = input('''Выбери действие:
    1 - В бой!  
    2 - Информация об матиматичке  
    3 - инвентарь  //в разработке
    4 - столовка  //в разработке
    5 - взять взятку 
    6 - уйти на плонёрку
ваш ответ: ''')
    if player['rep'] <= 0:
        Print('вас вызвали к деректору за то что ваша репутация 0')
        Print('ВЫ УВОЛЕНЫ!!!!!')
        break
    if action == '2':
        info_pl()
    if action == '6':
        training()
    
    if action == '5':
        vzatka()
    if action == '1':
        cm=boy(cm)


