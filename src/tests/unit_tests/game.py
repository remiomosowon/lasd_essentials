class Player(object):
    def __init__(self, die1, die2):
        self.die1 = die1
        self.die2 = die2

    def roll_dice(self):
        self.die1.roll()
        self.die2.roll()
        fv1 = self.die1.get_face_value()
        fv2 = self.die2.get_face_value()
        return fv1, fv2

    def take_turn(self):
        pass

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def take_turn(self):
        fv1, fv2 = self.roll_dice()
        current_position = self.get_position()
        return self.board.get_new_position(fv1 + fv2, current_position)

    def set_board(self, board):
        self.board = board

class Board(object):
    BOARD_SIZE = 40

    def get_new_position(self, face_value, current_position):
        return (face_value + current_position) % Board.BOARD_SIZE

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