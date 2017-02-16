from behave import *

use_step_matcher("parse")


@given('we have {num_players} players')
def step_given_players(context, num_players):
    # context.game.set_players(num_players)
    pass


@given('they play {num_rounds} round')
def step_given_rounds(context, num_rounds):
    # context.game.set_rounds(num_rounds)
    pass


@when('they play a game')
def step_when_play_game(context):
    # context.game_result = context.game.play_game()
    pass


@then('the game result will be game ended after {num_turns} turns')
def step_then_game_result(context, num_turns):
    # assert context.game_result == "game ended after {} turns".format(num_turns)
    assert False


@then('the game result will be error: {error_message}')
def step_then_game_error(context, error_message):
    # assert context.game_result == error_message
    assert False