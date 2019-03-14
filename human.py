"""
Subclass of the Player super class, used to implement
player activity
"""

from playing.utils.framework import Player

# Author: Dylan DeChiara
# Date: 3/11/19
# Version: 1.0

class HumanPlayer(Player):

    """
    The HumanPlayer class is a sub class of the Player class
    created in the framework.
    """

    def __init__(self, maximize):
        self.maximize = maximize
        self.opponent = None

    def maximizes(self):
        return self.maximize

    def assume(self, opponent):
        self.opponent = opponent

    def move(self, game, alpha=None, beta=None):
        moves = game.moves()
        print('Possible moves: ', moves)

        move = None
        while move not in moves:

            move = eval(input("Your choice: "))

        return move