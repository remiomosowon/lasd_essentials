import unittest

class Player(object):
    pass

class Board(object):
    pass

class Die(object):
    pass

class Game(object):

    def __init__(self):
        self.board = Board()
        self.die1 = Die()
        self.die2 = Die()
        self.players = []
        self.rounds = 0

    def initialise(self, num_players, num_rounds):
        if num_players < 2:
            raise Exception

        for x in range(num_players):
            self.players.append(Player())

        self.rounds = num_rounds

class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()


    def test_initialise_empty_game(self):
        self.assertTrue(self.game.board is not None)
        self.assertTrue(self.game.die1 is not None)
        self.assertTrue(self.game.die2 is not None)
        self.assertTrue(self.game.players is not None)
        self.assertEquals(self.game.rounds, 0)

    def test_initialise_simple_game(self):
        self.game.initialise(num_players=2, num_rounds=1)
        self.assertEquals(self.game.rounds, 1)
        self.assertEquals(len(self.game.players), 2)

    def test_initialise_simple_game_without_enough_players(self):

        with self.assertRaises(Exception):
            self.game.initialise(num_players=1, num_rounds=1)


