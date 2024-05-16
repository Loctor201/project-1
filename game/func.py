from data import *
from time import *
def Print(str0):
    print()
    s0 = ''
    for i in str0:
        s0 += i
        print("\033[F" + s0)
        sleep(0.05)
def info_pl():
    print(f'професия - {player["name"]}')
    print(f'здоровье - {player["hp"]}')
    print(f'урон - {player["damage"]}')
    print(f'защита - {player["defence"]}')
    print(f'оружие - {player["weapon"]}')
    print(f'репутация - {player["rep"]}')
    print(f'деньги - {player["money"]}')
    sleep(1)
def training():
    a = randint(1,3)
    print('деректор расказал вам как надо висти себя с учениками')
    for q in range(2):
        Print('блаблабла блаблабла блаблабла блаблабла блаблабла блаблабла блаблабла блаблабла ')
    print('ваш урон повысен на', a)
    player['damage'] += a
    sleep(1)
def vzatka():
    player['money'] += 100
    Print('вы взяли 100Р')
    player['rep'] -= 1
    Print('ваша репутация понижена на 1')
    sleep(1)
def boy(cm0):
    e=vrag[cm0]
    print(e['name'],':',e['script'])
    while player['hp']>0 and e['hp']>0:
        player['hp'] -=e['attack']
        e['hp'] -=player['damage']
        print(f'твоё HP {player["hp"]}, HP врага {e["hp"]}, враг нонёс {e["attack"]}, вы нанесли {player["damage"]}')
    if e['hp']<=0:
        print(e['win'])
        cm0+=1
    else:
        print(e['loss'])
    return cm0

        
