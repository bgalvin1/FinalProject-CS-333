import unittest
from computer import Computer

class TestComputer(unittest.TestCase):

    def test_getScore_emptyScore(self):
        c = Computer()
        self.assertEqual(c.getScore(), 0)
    
    def test_computerMove(self):
        c = Computer()
        m = c.computerMove()
        if m == 'rock':
            self.assertEqual(m, 'rock')
        elif m == 'paper':
            self.assertEqual(m, 'paper')
        elif m == 'scissors':
            self.assertEqual(m, 'scissors')
        else:
            self.assertEqual(0, 1)

if __name__ == '__main__':
    unittest.main()
