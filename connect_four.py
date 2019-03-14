"""
This class ('connect_four') implements the commonly known
connect four game, where the object of the game is to be the
first player to get 4 pieces in a row in any direction.
"""

from copy import deepcopy
from playing.utils.framework import Game

# Author: Dylan DeChiara
# Date: 3/11/19
# Version: 1.0

HEIGHT = 6
WIDTH = 7

# generate playing board as a 2d array based
# on both height and width

BOARD = []
for x in range(HEIGHT):

    if x == HEIGHT - 1:
        r = []
        for v in range(WIDTH):
            r.append(9)
    else:
        r = []
        for v in range(WIDTH):
            r.append(0)

    BOARD.append(r)

class ConnectFour(Game):

    """
    The ConnectFour class takes a Game object and outlines all the needed attributes
    to both play out and evaluate the game during any instance
    """

    def __init__(self, last_player=None, board=BOARD):
        self.board = board
        self.player = last_player

    def __eq__(self, other):

        """
        Determine if self (board) and other(board) are
        equal

        :param other: board data structure we're comparing
        self.board to
        :return: true if equal false if not
        """

        return self.board == other.board

    def __hash__(self):

        """
        Uniquely identifies a board with a hash value

        :return: Hash value of self.board to provide a unique
        identifier for the board itself
        """

        return hash(str(self.board))

    def child(self, move, player):

        """
        Takes both a move and a player to create and return a new
        board with the passed in move and fills in 'move' location
        with either 1 or 2 based on if the player is maximized or not

        :param move: location on the board where player is
        allowed to put a piece
        :param player: current Player with valid move that is being
         passed in
        :return: ConnectFour class object with passed in player and a newly
        generated deepcopied board (child) based on the move that has been passed in
        """

        (row, col) = move

        copy_board = deepcopy(self.board)

        # checks what player is playing
        if player.maximizes():
            copy_board[row][col] = 1
        else:
            copy_board[row][col] = 2

        return ConnectFour(player, copy_board)

    def utility(self):

        """
        Determines if the game is over
        :return: either 1 (maximized player has won), -1 (maximized player has lost), and 0 if
        the game has ended in a tie
        """

        # -1 0 +1 for win / loss
        return check_victory(self.board)

    def display(self):

        """
        Method that prints the game out in a readable and
         user friendly fashion. Translating the board from 0s, 1s, and 2s
         to "-", "Xs", or "Ys"
        :return: User friendly observable version of the game and player moves
        """

        #player UI
        s = "  "
        for p in range(WIDTH):
            s += str(p)
            s += " "

        print(s)

        for row in range(HEIGHT):

            # player UI
            print(row, end=' ')

            for col in range(WIDTH):

                if self.board[row][col] == 1:
                    print("X", end=' ')
                elif self.board[row][col] == 2:
                    print("O", end=' ')
                else:
                    print("-", end=' ')
            print()

    def moves(self):

        """
        Generate a list of moves based on the pieces on the board
        and the rules of connect four.

        :return: A list of moves based on the locations of current
        player (self) pieces on the board
        """

        moves = list()

        for row in range(HEIGHT):
            for col in range(WIDTH):

                move = (row, col)

                if self.board[row][col] == 9:
                    moves.append(move)

                if self.board[row][col] == 1 or self.board[row][col] == 2:

                    move = (row - 1, col)

                    if self.board[row - 1][col] == 1 or self.board[row - 1][col] == 2:

                        pass

                    else:

                        moves.append(move)

        return moves

def check_victory(board):

    """
    Called by utility function.

    Determines of there is either a win condition (game has been won or lost
    depending on the player and if they have maximized) on the board,
    open spots, or if there are no longer any open spots on the board
    and therefore the game has resulted in a tie.

    :param board: Current board with designated moves from both players
    :return: 1 if maximized player has won, -1 if non-maximized player has won (maximized player
    lost), 0 if game finishes in a tie, and none if there are still moves left.
    """

    for row in range(HEIGHT):
        for col in range(WIDTH):

            player = board[row][col]

            # not a player move
            if player == 0 or player == 9:
                continue

            # look right
            if col + 3 < WIDTH and player == board[row][col + 1] and player == board[row][col + 2]\
                    and player == board[row][col + 3]:
                if player == 1:
                    return +1
                else:
                    return -1

            if row + 3 < HEIGHT:

                # down
                if player == board[row + 1][col] and player == board[row + 2][col] and player == board[row + 3][col]:
                    if player == 1:
                        return +1
                    else:
                        return -1

                # down and right
                if col + 3 < WIDTH and player == board[row + 1][col + 1] and player == board[row + 2][col + 2]\
                        and player == board[row + 3][col + 3]:
                    if player == 1:
                        return +1
                    else:
                        return -1

                # down and left
                if col - 3 >= 0 and player == board[row + 1][col - 1] and player == board[row + 2][col - 2] \
                        and player == board[row + 3][col - 3]:
                    if player == 1:
                        return +1
                    else:
                        return -1


        # # if no one has won yet
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if board[row][col] == 0 or board[row][col] == 9:
                return None

    return 0






