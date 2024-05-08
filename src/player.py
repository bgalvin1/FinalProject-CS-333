#set up the player class, function for playing a move. Function for displaying move, score stored for multiple rounds
#import numpy as np
class Player:
    score = 0
    moveset = ['paper', 'rock', 'scissors']

    def playerMove(self, move):
        if move <= 2:
            return self.moveset[move]
        else: 
            return -1
    
    def getScore(self):
        return self.score