from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))

from monopoly.game import Game

def before_scenario(context, scenario):
    context.game = Game()
    game = Game()
    game.initialise(num_players=2, num_rounds=1)
    context.player = game.players[0]
