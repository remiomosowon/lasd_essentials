Feature: Take Turn


  Scenario Outline: Player takes a turn
    Given we have a player position <initial_position>
    # player rolls dice
    When player moves token by total dice face value of <dice_value>
    Then the final position of the player will be <final_position>

    Examples:
      | initial_position | dice_value | final_position |
      | 1                | 2          | 3              |
      | 39               | 2          | 1              |
      | 1                | 12         | 13             |