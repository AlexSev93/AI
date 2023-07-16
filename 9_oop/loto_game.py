import random


class PC_Player:
    def __init__(self):
        self.card = []
        self.basic_name = 'PC_Player'
        self.sum_cask = 0
        while True:
            if len(self.card) == 15:
                break
            n = random.randint(1, 90)
            if n not in self.card:
                self.card.append(n)
        self.card = [self.card[0:5], self.card[5:10], self.card[10:]]
        for j in range(3):
            for i in range(4):
                pos = random.randint(0, 4 + i)
                self.card[j].insert(pos, '--')

    def show_card(self):
        for j in range(3):
            for i in range(9):
                print(f' {self.card[j][i]} ', end='')
            print('\n')

    def select_cask(self, num_cask):
        for j in self.card:
            if num_cask in j:
                j[j.index(num_cask)] = '--'
                self.sum_cask += 1
                break

    def win(self):
        if self.sum_cask == 15:
            return True


class Human_Player(PC_Player):
    def select_cask(self, num_cask):
        true_answer = 0
        for j in self.card:
            if num_cask in j:
                true_answer = 1
                break
        question = input(f'Ход игрока {self.basic_name}. Продолжить или зачеркнуть? п/з - ')
        if question == 'з' and true_answer == 1:
            row = int(input(f'В каком ряду число - {num_cask}? - ')) - 1
            col = int(input(f'В каком столбце число - {num_cask}? - ')) - 1
            if self.card[row][col] == num_cask:
                self.card[row][col] = '--'
                self.sum_cask += 1
            else:
                return True
        elif question == 'п' and true_answer == 1:
            return True
        elif question == 'п' and true_answer == 0:
            return False
        else:
            return True


if __name__ == '__main__':
    print('1. Играть компьютер/человек')
    print('2. Играть человек/человек ')
    print('3. Играть компьютер/компьютер')
    print('4. Играть n человек')
    game_mode = int(input('Выбрать режим игры - '))

    players = {}
    if game_mode == 1:
        player_name = input('Ввести имя игрока - ')
        players['Человек'] = Human_Player()
        players['Человек'].basic_name = player_name
        players['Компьютер'] = PC_Player()
        winner = [player_name, players['Компьютер'].basic_name]
    elif game_mode == 2:
        player_1_name = input('Ввести имя первого игрока - ')
        player_2_name = input('Ввести имя второго игрока - ')
        players[player_1_name] = Human_Player()
        players[player_2_name] = Human_Player()
        players[player_1_name].basic_name = player_1_name
        players[player_2_name].basic_name = player_2_name
        winner = [player_1_name, player_2_name]
    elif game_mode == 3:
        players['Компьютер_1'] = PC_Player()
        players['Компьютер_1'].basic_name = 'PC_Player_1'
        players['Компьютер_2'] = PC_Player()
        players['Компьютер_2'].basic_name = 'PC_Player_2'
        winner = ['PC_Player_1', 'PC_Player_2']
    elif game_mode == 4:
        winner = []
        count_plauers = int(input('Ввести количество игроков - '))
        for i in range(count_plauers):
            player_name = input(f'Ввести имя игрока №{i + 1} - ')
            players[player_name] = Human_Player()
            players[player_name].basic_name = player_name
            winner.append(player_name)
    else:
        print('Нет такого в меню')

    bag = []
    while True:
        if len(bag) == 90:
            break
        num = random.randint(1, 90)
        if num not in bag:
            bag.append(num)

    losers = []
    for i in range(90):
        print(f'------------------ Ход номер {i + 1}, бочонок с номером {bag[i]} ------------------')
        for key in players.keys():
            if key not in losers:
                print(f'------------------ Карта игрока {key} ------------------')
                players[key].show_card()

        for key in players.keys():
            if key not in losers:
                if players[key].select_cask(bag[i]):
                    print(f'Проиграл игрок {players[key].basic_name}')
                    losers.append(key)
                elif players[key].win():
                    print(f'Победил игрок {players[key].basic_name}')
                    exit = 1
        if len(winner) - len(losers) == 1:
            for i in losers:
                winner.remove(i)
            print(f'Победил игрок {winner[0]}')
            break
        if exit == 1:
            break
