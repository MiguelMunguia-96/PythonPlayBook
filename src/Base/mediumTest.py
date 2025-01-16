import unittest

from medium import *

class TestBaseMedium(unittest.TestCase):
    def test_minionGame(self):
        self.assertEqual(minion_game("BANANA"), "Stuart 12.0")
        self.assertEqual(minion_game(""), 0)
        self.assertEqual(minion_game("BANANANAAAS"), "Draw")
        self.assertEqual(minion_game("BANANANAEEEAAS"), "Kevin 60")


        


if __name__ == '__main__':
    unittest.main()