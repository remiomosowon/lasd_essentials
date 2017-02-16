import unittest
from monopoly.game import *


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

    def test_initiliase_simple_game_players_have_board(self):
        self.game.initialise(num_players=2, num_rounds=1)

        self.assertIs(self.game.players[0].board, self.game.board)
