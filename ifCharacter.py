import unittest
import tictactoe as tt

class ifCharacter(unittest.TestCase):
    board = tt.Board()
    def test_not_chara(self):
        self.assertEqual(self.board.if_character('Y'), False)

    def test_is_chara(self):
        self.assertEqual(self.board.if_character('X'), True)

    def test_isnot_chara(self):
        self.assertEqual(self.board.if_character('NOT'), False)


if __name__ == '__main__':
    unittest.main()
