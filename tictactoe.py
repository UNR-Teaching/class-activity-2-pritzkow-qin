""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""
import numpy as np

class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.board = np.array([['A','A','A'],['A','A','A'],['A','A','A']])
        pass

    def mark_square(self, column, row, player):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param player: (str) the X or O representation of which player to mark in square

        :return: ????
        """
        self.board[row][column] = player
        return self.board

        pass

    def has_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: ????
        """
        if self.col_check('X') == True:
            return True, 'X'
        elif self.row_check('X') == True:
            return True, 'X'
        elif self.diag_check('X') == True:
            return True, 'X'
        elif self.col_check('O') == True:
            return True, 'O'
        elif self.row_check('O') == True:
            return True, 'O'
        elif self.diag_check('O') == True:
              return True, 'O'
        else:
            return False

        pass

    def row_check(self, player):
        for x in range(len(self.board)):
            win = True

            for y in range(len(self.board)):
                if self.board[x,y] != player:
                    win = False

            if win == True:
                return win

        return win

    def col_check(self, player):
        for x in range(len(self.board)):
            win = True

            for y in range(len(self.board)):
                if self.board[y][x] != player:
                    win = False
                    continue

            if win == True:
                return win
        return win

    def diag_check(self, player):
        win = True

        for x in range(len(self.board)):
            if self.board[x,x] != player:
                win = False
        return win

    def play_game(self):
        """
        Takes moves from raw_input as comma-separated list in form (column, row, player)
            and makes a move. When a winner has been determined, the game ends

        :return: (str) the letter representing the player who won
        """
        win = False

        while not win:
            col = input('Enter Column(0-2)')
            row = input('Enter Row(0-2)')
            if not self.in_bound(row, col):
                print('Out of Bounds Try Again')
                break
            player = input('Enter Player: ')
            if not self.if_character(player):
                print('Not Valid Player')
                break

            self.mark_square(col, row, player)
            win, winner = self.has_winner()

        return winner 
        pass

    def in_bound(self, row, col):
        if row > 2 or col > 2:
            return False
        else:
            return True
        pass

    def if_character(self, player):
        if player == 'X' or player == 'O':
            return True
        else:
            return False
        pass

if __name__ == '__main__':
    board = Board()
    print(board.mark_square(0,0,'X'))
    print(board.mark_square(1,0,'X'))
    print(board.mark_square(2,0,'X'))
    print(board.mark_square(0,0,'X'))
    print(board.mark_square(1,1,'X'))
    print(board.mark_square(2,2,'X'))

    print(board.row_check('X'))
    print(board.col_check('X'))
    print(board.diag_check('X'))
    # winner = board.play_game()
    # print("{} has won!".format(winner))

