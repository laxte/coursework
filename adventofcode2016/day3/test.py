import unittest
import day3

class TestSquaresWithThreeSides(unittest.TestCase):

   def test_1_2_2_is_triangle(self):
       self.assertTrue(day3.isAValidTriangle(['1','2','2']))

   def test_1_2_4_is_not_triangle(self):
       self.assertFalse(day3.isAValidTriangle(['1','2','4']))

   def test_3_3_5_is_triangle(self):
       self.assertTrue(day3.isAValidTriangle(['3','3','5']))

   def test_3_3_6_is_not_triangle(self):
       self.assertFalse(day3.isAValidTriangle(['3','3','6']))

   def test_3_3_7_is_not_triangle(self):
       self.assertFalse(day3.isAValidTriangle(['3','3','7']))

   def test_123_453_237_is_not_triangle(self):
       self.assertFalse(day3.isAValidTriangle(['123','453','237']))


if __name__ == '__main__':
   unittest.main()
