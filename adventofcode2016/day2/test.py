import unittest
import day2b

#    1
#  2 3 4
#5 6 7 8 9
#  A B C
#    D



class TestToiletCode(unittest.TestCase):

   def test_UpFrom5Returns5(self):
       location = [2,0]
       element = day2b.moveOnKeyPad('U',location)
       self.assertEqual([2,0],location)

def test_RightFrom5Returns6(self):
       location = [2,0]
       element = day2b.moveOnKeyPad('R',location)
       self.assertEqual([2,1],location)

   def test_LeftFrom8Returns7(self):
       location = [2,3]
       element = day2b.moveOnKeyPad('L',location)
       self.assertEqual([2,2],location)

   def test_DownFrom1Returns3(self):
       location = [0,2]
       element = day2b.moveOnKeyPad('D',location)
       self.assertEqual([1,2],location)

   def test_RightFrom9Returns9(self):
       location = [2,4]
       element = day2b.moveOnKeyPad('R',location)
       self.assertEqual([2,4],location)

if __name__ == '__main__':
   unittest.main()
