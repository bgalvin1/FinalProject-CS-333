from computer import Computer
from player import Player
#take input from player
#method for computing result + giving score
#method for computing best 2 out of 3 victor

class Game:
    c = Computer()
    p = Player()

    #0 for player win 1 for CPU win -1 tie
    def computeWinner(self, playermove, computermove):
        if (playermove == 'rock' and computermove == 'scissors'):
            self.p.score += 1
            return 0
        elif (playermove == 'paper' and computermove == 'rock'):
            self.p.score += 1
            return 0
        elif (playermove == 'scissors' and computermove == 'paper'):
            self.p.score += 1
        elif (playermove == 'rock' and computermove == 'paper'):
            self.c.score += 1
            return 1
        elif(playermove == 'paper' and computermove == 'scissors'):
            self.c.score += 1
            return 1
        elif(playermove == 'scissors' and computermove == 'rock'):
            self.c.score += 1
            return 1
        else:
            return -1
        
    #0 for player win 1 for CPU win
    def computeBestOf3(self):
        if (self.p.score == 2):
            return 0
        if (self.c.score == 2):
            return 1

def main():
    g = Game()
    while(g.computeBestOf3() != 1 or 0):
        option = int(input("Choose a move, 0:rock 1: paper 2: scissors"))
        playermove = g.p.playerMove(option)
        computerMove = g.c.computerMove()
        outcome = g.computeWinner(playermove, computerMove)
        if outcome == 0:
            print("computer move your move: " + computerMove + "Your move: " + playermove)
            print("you won round the round\n")
            print(f"Your score: {g.p.getScore()} Computer Score: {g.c.getScore()}")
        else:
            print("computer move your move: " + computerMove + "Your move: " + playermove)
            print("computer won the round \n")
            print(f"Your score: {g.p.getScore()} Computer Score: {g.c.getScore()}")
    if g.computeBestOf3 == 1:
        print("You won the game!")
    else:
        print("You lost, better luck next time!")

if __name__ == "__main__":
    main()