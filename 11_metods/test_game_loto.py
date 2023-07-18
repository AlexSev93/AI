from players_class import PC_Player, Human_Player, Interface


class Test_PC_Player:
    def test_init(self):
        pc_player = PC_Player()
        assert pc_player.get_basic_name() == 'PC_Player'
        test_card = pc_player.get_card()
        assert len(test_card) == 3
        for i in test_card:
            assert len(i) == 9

        num = []
        for i in test_card:
            num.extend(i)
        assert len(set(num)) == 16
        assert pc_player.get_sum_cask() == 0

    def test_select(self):
        pc_player = PC_Player()
        n = [i for i in range(1, 91)]
        for i in n:
            pc_player.select_cask(i)
        test_card = pc_player.get_card()
        num = []
        for i in test_card:
            num.extend(i)
        assert len(set(num)) == 1
        assert pc_player.get_sum_cask() == 15

    def test_win(self):
        pc_player = PC_Player()
        pc_player.set_sum_cask(15)
        assert pc_player.win()

    def test_get_set(self):
        pc_player = PC_Player('Max')
        assert pc_player.get_basic_name() == 'Max'
        assert isinstance(pc_player.get_card(), list)
        assert pc_player.get_sum_cask() == 0
        pc_player.set_sum_cask(2)
        assert 2 == pc_player.get_sum_cask()

        pc_player.set_basic_name('TEST')
        assert pc_player.get_basic_name() == 'TEST'

    def test_eq(self):
        pc_player1 = Human_Player('A')
        pc_player1.set_sum_cask(4)
        pc_player2 = Human_Player('B')
        pc_player2.set_sum_cask(4)
        assert pc_player1 == pc_player2


class Test_Human_Player:
    def test_true_answer(self):
        human_player = Human_Player()
        test_card = human_player.get_card()
        num = []
        for i in test_card:
            num.extend(i)
        num = list(set(num))
        num.remove('--')
        assert human_player._true_answer(num[0]) == 1
        assert human_player.human_select_cask(num[0], 'п') == True
        assert human_player.human_select_cask(0, 'п') == False
        assert human_player.human_select_cask(0, 'з') == True
        assert human_player.human_select_cask(num[0], '') == True


class Test_Interface:
    def test_select_game_mode(self):
        test_interface = Interface()
        assert test_interface.select_game_mode(5) == 'Exit'
        a, b, c = test_interface.select_game_mode(3)
        assert type(a) == dict
        assert type(b) == list and len(b) == 2
        assert c == []
        assert type(a['Компьютер_1']) == PC_Player and type(a['Компьютер_2']) == PC_Player

    def test_show_menu(self):
        test_interface = Interface()
        assert type(test_interface.show_menu()) == str
