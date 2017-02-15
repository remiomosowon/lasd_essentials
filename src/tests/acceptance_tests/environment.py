class Game(object):
    def __init__(self):
        pass

    def set_players(self, players):
        pass

    def set_rounds(self, rounds):
        pass

    def play_game(self):
        return "A Game"


def before_scenario(context, scenario):
    context.game = Game()
