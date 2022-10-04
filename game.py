from player import Player
from dice import Dice
def main():
    #globals
    game_end = False

    #instatiate the player
    player1 = Player()

    #main game loop
    while game_end == False:
        if game_end == False:
            decision = input('Roll dice? [y/n] ')

            if decision.lower() == 'y':
                # instantiates a dice
                dice = Dice()
                rolls = dice.set_rolls()
                good_roll = 0
                outcome_string = 'You rolled:'
                for roll in rolls:
                    if roll == 1:
                        player1.points += 100
                        good_roll += 1
                    elif roll == 5:
                        player1.points += 50
                        good_roll += 1
                    outcome_string += f' {roll}'
                if good_roll == 0:
                    game_end = True
                print(outcome_string)
                print(f'Your score is {player1.points}')
                print()

            elif decision.lower() == 'n':
                game_end = True

            else:
                print('That input is not valid.')

if __name__ == '__main__':
    main()