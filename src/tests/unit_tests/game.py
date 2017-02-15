class Player(object):
    def __init__(self, die1, die2):
        self.die1 = die1
        self.die2 = die2

    def take_turn(self):
        pass

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_board(self, board):
        self.board = board

class Board(object):
    def get_new_position(self, face_value, current_position):
        new_position = face_value + current_position
        if new_position > 40:
            new_position = new_position - 40

        return new_position

class Die(object):
    def roll(self):
        pass

    def get_face_value(self):
        return 0

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