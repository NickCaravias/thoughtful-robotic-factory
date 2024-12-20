import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sort import sort

class TestSort(unittest.TestCase):
    def test_standard_package(self):
        # Small, light package
        self.assertEqual(sort(10, 10, 10, 10), "standard")
        
    def test_special_package_by_volume(self):
        # Bulky by volume (1,000,000 cm³)
        self.assertEqual(sort(100, 100, 100, 10), "special")
        
    def test_special_package_by_dimension(self):
        # bulky
        self.assertEqual(sort(150, 10, 10, 10), "special")
        
    def test_special_package_by_mass(self):
        # heavy 
        self.assertEqual(sort(10, 10, 10, 20), "special")
        
    def test_rejected_package(self):
        # bulky and heavy
        self.assertEqual(sort(150, 150, 150, 25), "rejected")
        
    def test_edge_cases(self):
        # most amount of volume
        self.assertEqual(sort(100, 100, 100, 19), "special")
        #  most amount of mass
        self.assertEqual(sort(10, 10, 10, 20), "special")

    def test_negative(self):
        # negative values
        self.assertEqual(sort(-10, -10, -10, -10), "rejected")
        self.assertEqual(sort(-150, -150, -150, -25), "rejected")

if __name__ == '__main__':
    unittest.main()