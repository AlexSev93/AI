import random


class PC_Player:
    def __init__(self, basic_name='PC_Player'):
        self._card = []
        self._basic_name = basic_name
        self._sum_cask = 0
        while len(self._card) != 15:
            n = random.randint(1, 90)
            if n not in self._card:
                self._card.append(n)
        self._card = [self._card[0:5], self._card[5:10], self._card[10:]]
        for j in range(3):
            for i in range(4):
                pos = random.randint(0, 4 + i)
                self._card[j].insert(pos, '--')

    def show_card(self):
        for i in range(3):
            line = ' '.join(map(str, self._card[i]))
            print(line)

    def select_cask(self, num_cask):
        for j in self._card:
            if num_cask in j:
                j[j.index(num_cask)] = '--'
                self._sum_cask += 1
                break

    def win(self):
        if self._sum_cask == 15:
            return True

    def get_basic_name(self):
        return self._basic_name

    def get_card(self):
        return self._card

    def get_sum_cask(self):
        return self._sum_cask

    def set_sum_cask(self, new_sum_cask):
        self._sum_cask = new_sum_cask


class Human_Player(PC_Player):
    def true_answer(self, _num_cask):
        true_answer = 0
        for j in self._card:
            if _num_cask in j:
                true_answer = 1
                break
        return true_answer

    def human_select_cask(self, _num_cask, answer_human):
        if answer_human == 'з' and self.true_answer(_num_cask) == 1:
            while True:
                try:
                    row = int(input(f'В каком ряду число - ? - ')) - 1
                except ValueError:
                    print('Вводим только числа')
                else:
                    break
            while True:
                try:
                    col = int(input(f'В каком столбце число - ? - ')) - 1
                except ValueError:
                    print('Вводим только числа')
                else:
                    break
            if self._card[row][col] == _num_cask:
                self._card[row][col] = '--'
                self._sum_cask += 1
            else:
                return True
        elif answer_human == 'п' and self.true_answer(_num_cask) == 0:
            return False
        else:
            return True
