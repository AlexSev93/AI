from players_class import Human_Player, PC_Player
import random


print('1. Играть компьютер/человек')
print('2. Играть человек/человек ')
print('3. Играть компьютер/компьютер')
print('4. Играть n человек')
print('5. Выход из программы')

while True:
    game_mode = int(input('Выбрать режим игры - '))
    players = {}
    winner = []
    losers = []
    end_game = 0
    if game_mode == 1:
        player_name = input('Ввести имя игрока - ')
        players[player_name] = Human_Player(player_name)
        print(type(players[player_name]))
        players['Компьютер'] = PC_Player()
        winner = [player_name, players['Компьютер'].get_basic_name()]
    elif game_mode == 2:
        player_1_name = input('Ввести имя первого игрока - ')
        player_2_name = input('Ввести имя второго игрока - ')
        players[player_1_name] = Human_Player(player_1_name)
        players[player_2_name] = Human_Player(player_2_name)
        winner = [player_1_name, player_2_name]
    elif game_mode == 3:
        players['Компьютер_1'] = PC_Player('PC_Player_1')
        players['Компьютер_2'] = PC_Player('PC_Player_2')
        winner = ['PC_Player_1', 'PC_Player_2']
    elif game_mode == 4:
        winner = []
        while True:
            try:
                count_plauers = int(input('Ввести количество игроков - '))
                if count_plauers > 2:
                    break
                else:
                    print('Игроков больше 2х')
            except ValueError:
                print('Вводим только числа')
        for i in range(count_plauers):
            player_name = input(f'Ввести имя игрока №{i + 1} - ')
            players[player_name] = Human_Player(player_name)
            winner.append(player_name)
    elif game_mode == 5:
        break
    else:
        print('Нет такого в меню')

    bag = []
    while True:
        if len(bag) == 90:
            break
        num = random.randint(1, 90)
        if num not in bag:
            bag.append(num)

    for i in range(90):
        print(f'------------------ Ход номер {i + 1}, бочонок с номером {bag[i]} ------------------')
        for key in players.keys():
            if key not in losers:
                print(f'------------------ Карта игрока {key} ------------------')
                players[key].show_card()

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
