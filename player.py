import math
from multiprocessing.sharedctypes import Value
import random

class Player:
    def __init__(self,letter):
        #letter is x or o
        self.letter = letter

    #in order to players move 
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self, game):
        #get a random valid spot for PC next move
        square = random.choice(game.available_moves())
        return square

class HummanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False #user do not entered valid key yet
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-8)')
            #we are going to check that this is a correct value by trying to cast
            #it to an integer, and if it is not, then we say its invalid
            #if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True #if these are successful, then good
            except ValueError:
                print('Invalid square')

        return val



    