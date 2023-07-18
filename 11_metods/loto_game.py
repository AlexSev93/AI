import random
from players_class import Human_Player, Interface

interface = Interface()
print(interface.show_menu())

while True:
    game_mode = int(input('Выбрать режим игры - '))

    if interface.select_game_mode(game_mode) == 'Exit':
        break
    else:
        players, winner, losers = interface.select_game_mode(game_mode)
        break

if 0 < game_mode < 4:
    bag = []
    while True:
        if len(bag) == 90:
            break
        num = random.randint(1, 90)
        if num not in bag:
            bag.append(num)

    end_game = 0
    for i in range(90):
        print(f'------------------ Ход номер {i + 1}, бочонок с номером {bag[i]} ------------------')
        for key in players.keys():
            if key not in losers:
                print(f'------------------ Карта игрока {key} ------------------')
                print(players[key])

        for key in players.keys():
            if key not in losers:
                if isinstance(players[key], Human_Player):
                    question = input(f'Ход игрока {players[key].get_basic_name()}. Продолжить или зачеркнуть? п/з - ')
                    if players[key].human_select_cask(bag[i], question):
                        print(f'Проиграл игрок {players[key].get_basic_name()}')
                        losers.append(key)
                    elif players[key].win():
                        print(f'Победил игрок {players[key].get_basic_name()}')
                        end_game = 1
                else:
                    if players[key].select_cask(bag[i]):
                        print(f'Проиграл игрок {players[key].get_basic_name()}')
                        losers.append(key)
                    elif players[key].win():
                        print(f'Победил игрок {players[key].get_basic_name()}')
                        end_game = 1
        if len(winner) - len(losers) == 1:
            for los in losers:
                winner.remove(los)
            print(f'Победил игрок {winner[0]}')
            break
        if end_game == 1:
            break
