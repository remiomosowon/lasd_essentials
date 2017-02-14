Feature: play a game of monopoly


  Scenario Outline: Happy cases
    Given we have <num_players> players
    And they play <num_rounds> round
    When they play a game
    Then the game result will be game ended after <num_turns> turns

  Examples:
    | num_players | num_rounds | num_turns |
    | 2           | 1          | 2         |
    | 2           | 99         | 198       |
    | 8           | 99         | 792       |


  Scenario Outline: Incorrect number of players
    Given we have <num_players> players
    And they play <num_rounds> round
    When they play a game
    Then the game result will be error: <error_message>

  Examples:
    | num_players | num_rounds | error_message      |
    | 1           | 1          | not enough players |
    | 2
