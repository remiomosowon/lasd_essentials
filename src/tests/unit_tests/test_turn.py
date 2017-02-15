import unittest

from game import Die, Player, Board

class DeterministicDie(Die):

    def get_face_value(self):
        return 1

class TurnTest(unittest.TestCase):

    def setUp(self):
        die1 = DeterministicDie()
        die2 = DeterministicDie()
        board = Board()
        self.player = Player(die1, die2)
        self.player.set_board(board)

    def test_take_turn_at_position_1(self):
        self.player.set_position(1)
        fv1, fv2 = self.player.get_roll_dice()
        current_position = self.player.get_position()

        position = self.player.board.get_new_position(fv1 + fv2, current_position)

        self.assertEquals(position, 3)

    def test_take_turn_at_position_40(self):
        self.player.set_position(40)
        fv1, fv2 = self.player.get_roll_dice()
        current_position = self.player.get_position()
        position = self.player.board.get_new_position(fv1 + fv2, current_position)
        self.assertEquals(position, 2)
