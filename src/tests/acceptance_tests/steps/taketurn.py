from behave import *
use_step_matcher("parse")

@given('we have a player position {initial_position}')
def step_given_player_position(context, initial_position):
    context.player.token_position = initial_position


@when('player moves token by total dice face value of {dice_value}')
def step_when_player_rolls_dice(context, dice_value):
    context.player.move_token_by(dice_value)


@then('the final position of the player will be <final_position>')
def step_then_final_position(context, final_position):
    assert context.player.token_position == final_position
