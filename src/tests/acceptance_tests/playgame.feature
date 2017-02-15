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
      | 0           | 1          | not enough players |
      | 9           | 1          | too many players   |


  Scenario Outline: Incorrect number of rounds
    Given we have <num_players> players
    And they play <num_rounds> round
    When they play a game
    Then the game result will be error: <error_message>

    Examples:
      | num_players | num_rounds | error_message     |
      | 2           | 0          | not enough rounds |
      | 2           | 100        | too many rounds   |

  Scenario Outline: Incorrect number of rounds and players
    Given we have <num_players> players
    And they play <num_rounds> round
    When they play a game
    Then the game result will be error: <error_message>

    Examples:
      | num_players | num_rounds | error_message                         |
      | 1           | 100        | not enough players, too many rounds   |
      | 9           | 0          | too many players, not enough rounds   |
      | 1           | 0          | not enough players, not enough rounds |
      | 9           | 100        | too many players, too many rounds     |
