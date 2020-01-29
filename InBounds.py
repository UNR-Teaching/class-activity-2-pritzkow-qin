import unittest
import tictactoe as tt

class InBounds(unittest.TestCase):

    board = tt.Board()
    def test_Out_of_Bound(self):
        self.assertEqual(self.board.in_bound(3, 3), False)

    def test_in_Bound(self):
        self.assertEqual(self.board.in_bound(2, 2), True)

    def test_Out_of_Bound2(self):
        self.assertEqual(self.board.in_bound(3, 12), False)

if __name__ == '__main__':
    unittest.main()
