from players_class import PC_Player, Human_Player


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


class Test_Human_Player:
    def test_true_answer(self):
        human_player = Human_Player()
        n = [i for i in range(1, 91)]
        test_card = human_player.get_card()
        num = []
        for i in test_card:
            num.extend(i)
        num = list(set(num))
        num.remove('--')
        assert human_player.true_answer(num[0]) == 1
        assert human_player.select_cask(num[0], 'п') == True
        assert human_player.select_cask(0, 'п') == False
        assert human_player.select_cask(0, 'з') == True
        assert human_player.select_cask(num[0], '') == True




