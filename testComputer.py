import unittest
from computer import Computer

class TestComputer(unittest.TestCase):

    def test_getScore_emptyScore(self):
        c = Computer()
        self.assertEqual(c.getScore(), 0)
    
    def test_computerMove(self):
        c = Computer()
        self.assertEqual(c.computerMove(), 'rock' or 'paper' or 'scissors')

if __name__ == '__main__':
    unittest.main()
