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
        for x in range(num_players):
            self.players.append(Player())

        self.rounds = num_rounds

class GameTest(unittest.TestCase):
    def test_initialise_empty_game(self):
        game = Game()
        self.assertTrue(game.board is not None)
        self.assertTrue(game.die1 is not None)
        self.assertTrue(game.die2 is not None)
        self.assertTrue(game.players is not None)
        self.assertEquals(game.rounds, 0)

    def test_initialise_simple_game(self):
        game = Game()
        game.initialise(num_players=2, num_rounds=1)
        self.assertEquals(len(game.players), 2)
        self.assertEquals(game.rounds, 1)
