class Player:

    #the only attribute needed is points
    def __init__(self):
        self.points = 0

    #this comes in handy to give the player
    #an option to play again
    def reset_points(self):
        self.points = 0