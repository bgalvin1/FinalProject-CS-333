#computer player, method for random number between 0 and 2. Same attributes as player. 
from random import randrange
class Computer:
    score = 0
    moveset = ['paper', 'rock', 'scissors']

    def computerMove(self):
        return self.moveset[randrange(0,2)]
    
    def getScore(self):
        return self.score