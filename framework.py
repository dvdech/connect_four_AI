"""
Framework for both the Game and Player superclass'
"""

from time import sleep, time

# Author: Dylan DeChiara
# Date: 3/11/19
# Version: 1.0

# Super class for all games
class Game(object):

    """
    The Game class is the super class for all other
    Game objects, and outlines all necessary methods
    needed for a Game object to function properly.
    """

    # return whether this game is equivalent to another
    def __eq__(self, other):
        raise NotImplementedError

    # return a hash code for this game
    def __hash__(self):
        raise NotImplementedError

    # return the utility of this game (if it's over)
    def utility(self):
        raise NotImplementedError

    # Return a list of legal moves
    def moves(self):
        raise NotImplementedError

    # Return a new game created by a move
    def child(self, move, player):
        raise NotImplementedError

    # Print this game to the console
    def display(self):
        raise NotImplementedError

    # conduct this game
    def play(self, max_player, min_player, interval=1):

        """
        Conduct the specified game when given, a min and max player

        :param max_player: A Player that Maximizes
        :param min_player: A Player that Minimizes
        :param interval: Generic sleep time
        :return: The varying states of the game: ie move results
        per player and the finished state of the game.
        """

        print("Playing Game: ")
        self.display()
        moves = 0

        game = self
        player, opponent = max_player, min_player

        while game.utility() is None:

            start = time()
            move = player.move(game)
            seconds = time() - start

            if player.maximizes():
                print("MAX after ", seconds, " seconds: ")
            else:
                print("MIN after ", seconds, " seconds: ")

            game = game.child(move, player)
            game.display()
            moves += 1

            sleep(interval)
            player, opponent = opponent, player

        print("Game over with utility ", game.utility(), "after: ", moves, "moves.")




# Super class for all players
class Player(object):

    """
    The Player class is the super class for all other Player objects
    """

    # return whether this player wants to maximize utility
    def maximizes(self):
        raise NotImplementedError

    # return the move this play wants to make
    def move(self, game, alpha=None, beta=None):
        raise NotImplementedError


