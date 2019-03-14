"""
This class implements the minimax algorithm so that
it can be used when looking for possible connect four
moves.
"""

from playing.utils.framework import Player
from math import inf

# Author: Dylan DeChiara
# Date: 3/11/19
# Version: 1.0

class MiniMaxPlayer(Player):

    """
    Sub class of the Player superclass that frames the
    desired MiniMax player (either MIN or MAX)
    """

    def __init__(self):
        self.opponent = None

    # assign opponent
    def assume(self, opponent):
        self.opponent = opponent

    # check if player maximizes
    def maximizes(self):
        raise NotImplementedError

    # determines move
    def move(self, game, alpha=None, beta=None):
        return self.value(game)[1]

    # determines value for game and move
    def value(self, game):
        raise NotImplementedError

# Minimax framework for MAX player
class MaxPlayer(MiniMaxPlayer):

    def maximizes(self):
        return True

    # Return the best value and move for MAX in this game
    def value(self, game, alpha=-inf, beta=+inf):

        """
        Determine best value and move for MAX player

        :param game: Current game
        :param alpha: generic value for alpha beta pruning
        :param beta: generic value for alpha beta pruning
        :return: Best value and move for MAX player
        """

        # Is the game over?
        utility = game.utility()
        if utility is not None:
            return utility, None

        # Which move leads to the best outcome?
        best_value = -inf
        best_move = None

        for move in game.moves():
            child = game.child(move, self)
            value = self.opponent.value(child, alpha, beta)[0]

            # Maximizing
            if best_move is None or value > best_value:
                best_value = value
                best_move = move

            # Pruning
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break

        return best_value, best_move

# Minimax framework for MIN player
class MinPlayer(MiniMaxPlayer):

    def maximizes(self):
        return False

    # Return the best value and move for MIN in this game
    def value(self, game, alpha=-inf, beta=+inf):

        """
        Determine best value and move for MIN player

        :param game: Current game
        :param alpha: generic value for alpha beta pruning
        :param beta: generic value for alpha beta pruning
        :return: Best value and move for MIN player
        """

        # Is the game over?
        utility = game.utility()
        if utility is not None:
            return utility, None

        # Which move leads to the best outcome?
        best_value = +inf
        best_move = None

        for move in game.moves():
            child = game.child(move, self)
            value = self.opponent.value(child, alpha, beta)[0]

            # Minimizing
            if best_move is None or value < best_value:
                best_value = value
                best_move = move

            # Pruning
            beta = min(beta, best_value)
            if beta <= alpha:
                break

        return best_value, best_move
