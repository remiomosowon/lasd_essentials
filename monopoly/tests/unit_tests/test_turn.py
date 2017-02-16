import unittest
from monopoly.game import Die, Player, Board


class DeterministicDie(Die):
    def get_face_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class TurnTest(unittest.TestCase):
    ONE_SQUARE_AFTER_START = 2
    START_SQUARE = 1
    TWO_SQUARES_AFTER_START = 3
    LAST_SQUARE = 40
    MAX_SQUARE_REACHABLE_FROM_START = 13

    def setUp(self):
        self.die1 = DeterministicDie()
        self.die2 = DeterministicDie()
        board = Board()
        self.player = Player(self.die1, self.die2)
        self.player.set_board(board)

    def test_take_turn_from_start_square(self):
        self.die1.set_value(Die.MIN_DIE_VALUE)
        self.die2.set_value(Die.MIN_DIE_VALUE)
        self.player.set_position(TurnTest.START_SQUARE)

        position = self.player.take_turn()

        self.assertEquals(position, TurnTest.TWO_SQUARES_AFTER_START)

    def test_take_turn_from_last_square(self):
        self.die1.set_value(Die.MIN_DIE_VALUE)
        self.die2.set_value(Die.MIN_DIE_VALUE)
        self.player.set_position(TurnTest.LAST_SQUARE)

        position = self.player.take_turn()

        self.assertEquals(position, TurnTest.ONE_SQUARE_AFTER_START)

    def test_take_turn_with_max_dice_roll(self):
        self.die1.set_value(Die.MAX_DIE_VALUE)
        self.die2.set_value(Die.MAX_DIE_VALUE)
        self.player.set_position(TurnTest.START_SQUARE)

        position = self.player.take_turn()

        self.assertEquals(position, TurnTest.MAX_SQUARE_REACHABLE_FROM_START)
