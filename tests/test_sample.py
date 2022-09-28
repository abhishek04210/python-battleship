import sys
import unittest
sys.path.append('../')
from battleship.board import Board

class TestSampleClass(unittest.TestCase):

    def test_should_fail(self):
        self.fail('You should remove this test')
        
class TestBattleshipClass(unittest.TestCase):

    def test_plot_ship_vertically(self):
        board = Board(10, 10)
        board.plot_ship_vertically(1, 2, "ship0", 4)
        can_plot_ship = board.can_plot_ship_vertically(7, 5, 7)
        self.assertTrue(can_plot_ship)

    def test_plot_ship_horizontally(self):
        board = Board(10, 10)
        board.plot_ship_horizontally(2, 1, "ship0", 4)
        can_plot_ship = board.can_plot_ship_horizontally(5, 7, 7)
        self.assertTrue(can_plot_ship)

    def test_fail_plot_ship_vertically(self):
        board = Board(10, 10)
        board.plot_ship_vertically(1, 4, "ship1", 6)
        can_plot_ship = board.can_plot_ship_vertically(1, 4, 6)
        self.assertFalse(can_plot_ship)

    def test_fail_plot_ship_horizontally(self):
        board = Board(10, 10)
        board.plot_ship_horizontally(1, 4, "ship0", 4)
        can_plot_ship = board.can_plot_ship_horizontally(1, 4, 4)
        self.assertFalse(can_plot_ship)

    def test_hit_shot(self):
        board = Board(10, 10)
        board.plot_ship_horizontally(1, 4, "ship0", 4)
        shot = board.place_shot(1, 4)
        self.assertEqual(shot, "HIT")

    def test_sink_shot(self):
        board = Board(10, 10)
        board.plot_ship_horizontally(3, 4, "ship0", 4)
        shot = board.place_shot(3, 4)
        self.assertEqual(shot, "SINK")

    def test_water_shot(self):
        board = Board(10, 10)
        board.plot_ship_horizontally(3, 4, "ship0", 4)
        shot = board.place_shot(6, 4)
        self.assertEqual(shot, "WATER")
        

if __name__=="__main__":
    unittest.main()
