from players_class import PC_Player, Human_Player


def show_menu():
    menu_list = ['1. Играть компьютер/человек', '2. Играть человек/человек ',
                 '3. Играть компьютер/компьютер', '4. Играть n человек',
                 '5. Выход из программы']
    all_menu = ''
    for line in menu_list:
        all_menu = all_menu + line + '\n'
    return all_menu


def select_game_mode(game_mode):
    players = {}
    winner = []
    losers = []
    if game_mode == 1:
        player_name = input('Ввести имя игрока - ')
        players[player_name] = Human_Player(player_name)
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
                count_players = int(input('Ввести количество игроков - '))
                if count_players > 2:
                    break
                else:
                    print('Игроков больше 2х')
            except ValueError:
                print('Вводим только числа')
        for i in range(count_players):
            player_name = input(f'Ввести имя игрока №{i + 1} - ')
            players[player_name] = Human_Player(player_name)
            winner.append(player_name)
    elif game_mode == 5:
        return 'Exit'
    else:
        print('Нет такого в меню')

    return players, winner, losers


if __name__ == '__main__':
    print(show_menu())