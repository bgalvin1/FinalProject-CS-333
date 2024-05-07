import unittest
from player import Player

class TestPlayer(unittest.TestCase):

    def test_getScore_zero_score(self):
        n = Player()
        self.assertEqual(n.getScore(), 0)

    def test_playerMove_InRange(self):
        n = Player()
        self.assertEqual(n.playerMove(1), 'rock')
    
    def test_playerMove_OutOfRange(self):
        n = Player()
        self.assertEqual(n.playerMove(22), -1)

if __name__ == '__main__':
    unittest.main()
