import unittest
from pairfinderapp import heightaddsum

class Pruebas(unittest.TestCase):
    def test_simple_pair(self):
        """ test for a simple pair """

        self.assertEqual(heightaddsum(139)["Nate Robinson"], "Brevin Knight")
    
    def test_number_of_pairs(self):
        """ test for measure the number of pairs """

        self.assertEqual(len(heightaddsum(144)), 83)

    def test_no_pairs(self):
        """ test for no pairs """

        self.assertEqual(heightaddsum(1000), None)
    
    def test_single_record(self):
        """ test for single record """

        self.assertEqual(heightaddsum(151)["Antonio Daniels"], "Charlie Bell")
        self.assertNotEqual(heightaddsum(151)["Charlie Bell"], "Antonio Daniels")
    
    def test_duplicated_players(self):
        """ test for duplicates names """
        
        self.assertNotIn("Brevin Knight", heightaddsum(140).keys())
        

if __name__ == "__main__":
    unittest.main()