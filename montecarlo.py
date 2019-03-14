"""
This class ('monte_carlo) implements a simplified version
of the commonly known monte carlo tree search algorithm.
"""

import random
from playing.utils.framework import Player
from playing.players.minimax import MinPlayer, MaxPlayer

# Author: Dylan DeChiara
# Date: 3/11/19
# Version: 1.0

HEIGHT = 6
WIDTH = 7

class MonteCarlo(Player):


    """
    The MonteCarlo class takes a Player object and outlines
    all the required methods to determine the best move based on
    a calculated score create through x iterations of completed
    games that are generated.
    """

    def __init__(self, maximize):
        self.maximize = maximize
        self.opponent = None

    def assume(self, opponent):

        """
        Creates the player and opponent structure

        :param opponent: Another Player object
        :return: assign opponent as self's opponent
        """

        self.opponent = opponent

    def maximizes(self):

        """
        Determines if the player is maximized or not.
        Needed to determine whether or not a player has
        won or lost

        :return: True (MAX) or False (MIN)
        """

        return self.maximize

    def score(self, move, game):

        """
        Takes a move and the current game (board) and finishes the game by creating a
        dictionary of children and their respective utilities. Organizing moves based on
        whether or not they win, lose, tie, or do nothing.

        :param move: Tuple location of specific move in current game (board)
        :param game: Current orientation of the game
        :return: 1 if the game resulted in a win for MAX or MIN, -1 if the game resulted
        in a loss of MAX or MIN, and 0 if the game resulted in a tie. Also returns board size
        which is needed so we know when the board is small enough to enable Minimax protocol
        """

        board_size = 0

        game = game.child(move, self)

        p = self.opponent

        # get size of game
        for row in range(HEIGHT):
            for col in range(WIDTH):

                if game.board[row][col] == 0:
                    board_size += 1

        # while game is not finished
        while game.utility() is None:

            moves = game.moves()

            # dictionaries
            child_dict = dict()
            utility_dict = dict()
            winning_dict = dict()
            tie_dict = dict()
            open_board_dict = dict()
            losing_dict = dict()

            # create a key, value pair for each move and it's child
            for move in moves:

                child_dict[move] = game.child(move, p)

            # create a key, value pair for each move and it's utility
            for move, child in child_dict.items():

                utility_dict[move] = child.utility()

            # key: move value: utility
            # organize moves based on utilities
            for move, utility in utility_dict.items():

                # Check if p.maximize to see if 1 is a winning utility.

                if p.maximize is True and utility == 1:

                    winning_dict[move] = utility

                elif p.maximize is False and utility == -1:

                    winning_dict[move] = utility

                elif p.maximize is True and utility == -1:

                    losing_dict[move] = utility

                elif p.maximize is False and utility == 1:

                    losing_dict[move] = utility

                elif utility == 0:

                    tie_dict[move] = utility

                elif utility is None:

                    open_board_dict[move] = utility


            # empty dict eval to false bool(dict)
            # check dictionaries for possible moves

            # list of children with winning utility
            if bool(winning_dict):

                m = random.choice(list(winning_dict))

            else:

                # ties
                if bool(tie_dict):

                    m = random.choice(list(tie_dict))

                else:

                    # simply open board moves (no tie, loss, or win
                    if bool(open_board_dict):

                        m = random.choice(list(open_board_dict))

                    else:

                        # only possible move left
                        m = random.choice(list(losing_dict))


            game = game.child(m, p)

            # change p to simulate a back and forth between players
            if p is self:
                p = self.opponent
            else:
                p = self

        # check wins
        if self.maximize is True and game.utility() == 1:
            return 1, board_size

        elif self.maximize is False and game.utility() == -1:
            return 1, board_size

        # check ties
        elif game.utility() == 0:
            return 0, board_size

        # check loses
        elif self.maximize is True and game.utility() == -1:
            return -1, board_size

        elif self.maximize is False and game.utility() == 1:
            return -1, board_size


    def move(self, game, alpha=None, beta=None):

        """
        Determine the right move to makes by simulating x ('iterations) of
        fully played out games for each possible move per player. The goal
        here is to create a score for each move that is possible, where the higher
        the score the better the move will be in terms of winning the game.

        :param game: Current layout of the game
        :param alpha: Conditional args for alpha beta pruning (minimax)
        :param beta: Conditional args for alpha beta pruning (minimax)
        :return: The best possible move based on the score for each move possible
        """

        moves = game.moves()

        iterations = 300

        score = -iterations

        ret_move = None

        # go through each move of possible
        # moves and randomly make moves
        # till the game ends
        for move in moves:

            game_size_total = 0

            total = 0

            for x in range(iterations):

                # 1 0 -1
                scr, game_size = self.score(move, game)

                total += scr

                game_size_total += game_size

            # average size of game from current state
            avg_game_size = game_size_total / iterations


            #check if avg game size is <= 18
            #if player iS MINI and board is small enough for minimax alpha beta pruning
            if avg_game_size <= 18 and self.maximize is False:

                min_player = MinPlayer()
                max_player = MaxPlayer()

                min_player.assume(max_player)
                max_player.assume(min_player)

                value, ret_move = min_player.value(game)

            #check if avg game size is <= 18
            # if player iS MAX and board is small enough for minimax alpha beta pruning
            elif avg_game_size <= 18 and self.maximize is True:

                min_player = MinPlayer()
                max_player = MaxPlayer()

                min_player.assume(max_player)
                max_player.assume(min_player)

                value, ret_move = max_player.value(game)


            # check outputs to see if calculations and move aquistion is correct
            #print("score: ", score, "total: ", total, "move: ", move)

            # larger score is better

            # replace score with total if total is higher
            if total >= score:

                score = total
                ret_move = move


        # print(ret_move, total)

        # best move to return
        return ret_move