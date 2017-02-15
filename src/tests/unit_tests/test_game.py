import unittest

class Player(object):
    def __init__(self, die1, die2):
        self.die1 = die1
        self.die2 = die2

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
        if num_players < 2 or num_players > 8:
            raise Exception

        if num_rounds < 1 or num_rounds > 99:
            raise Exception

        for x in range(num_players):
            self.players.append(Player(self.die1, self.die2))


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

    def test_initialise_simple_game_with_too_many_players(self):

        with self.assertRaises(Exception):
            self.game.initialise(num_players=9, num_rounds=1)

    def test_initialise_simple_game_with_not_enough_rounds(self):
        with self.assertRaises(Exception):
            self.game.initialise(num_players=2, num_rounds=0)

    def test_initialise_simple_game_with_too_many_rounds(self):
        with self.assertRaises(Exception):
            self.game.initialise(num_players=2, num_rounds=100)

    def test_initialise_simple_game_players_have_dice(self):
        self.game.initialise(num_players=2, num_rounds=1)

        self.assertIs(self.game.players[0].die1, self.game.die1)
        self.assertIs(self.game.players[0].die2, self.game.die2)

        self.assertIs(self.game.players[1].die1, self.game.die1)
        self.assertIs(self.game.players[1].die2, self.game.die2)