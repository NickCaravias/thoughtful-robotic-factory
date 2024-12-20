import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sort import sort

class TestSort(unittest.TestCase):
    def test_standard_package(self):
        # Small and non bulky package
        self.assertEqual(sort(10, 10, 10, 10), "standard")
        
    def test_special_package_by_volume(self):
        # Bulky by volume (1,000,000 cm^3)
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

    def test_decimal(self):
        self.assertEqual(sort(10.5, 10.5, 10.5, 10.5), "standard")
        self.assertEqual(sort(10.5, 10.5, 10.5, 20.5), "special")
        self.assertEqual(sort(150.5, 150.5, 150.5, 25.5), "rejected")

    def test_negative(self):
        # negative values
        self.assertEqual(sort(-10, -10, -10, -10), "rejected")
        self.assertEqual(sort(-150, -150, -150, -25), "rejected")
    
    def test_zero(self):
        # test all zero inputs
        self.assertEqual(sort(0, 0, 0, 0), "standard")

    def test_non_float_parameters(self):
        # test non-float inputs
        self.assertEqual(sort("10", "10", "10", "10"), "rejected")
        self.assertEqual(sort(10, 10, 10, "10"), "rejected")
        self.assertEqual(sort(10, 10, "hello world", 10), "rejected")

if __name__ == '__main__':
    unittest.main()