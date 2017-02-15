import unittest

from game import Die, Player, Board

class DeterministicDie(Die):

    def __init__(self, value):
        self.value = value

    def get_face_value(self):
        return self.value


class TurnTest(unittest.TestCase):

    ONE_SQUARE_AFTER_START = 2
    START_SQUARE = 1
    TWO_SQUARES_AFTER_START = 3
    LAST_SQUARE = 40

    def setUp(self):
        die1 = DeterministicDie(1)
        die2 = DeterministicDie(1)
        board = Board()
        self.player = Player(die1, die2)
        self.player.set_board(board)

    def test_take_turn_from_start_square(self):
        self.player.set_position(TurnTest.START_SQUARE)

        position = self.player.take_turn()

        self.assertEquals(position, TurnTest.TWO_SQUARES_AFTER_START)

    def test_take_turn_from_last_square(self):
        self.player.set_position(TurnTest.LAST_SQUARE)

        position = self.player.take_turn()

        self.assertEquals(position, TurnTest.ONE_SQUARE_AFTER_START)
