from app.models.box import Box
from unittest import TestCase

class TestBox(TestCase):
    def test_standard_box(self):
        box = Box(100, 100, 10, 10)
        self.assertEqual("STANDARD", box.sort())
    
    def test_special_box(self):
        self.assertEqual("SPECIAL", Box(100, 100, 100, 10).sort())
        self.assertEqual("SPECIAL", Box(10, 100, 100, 20).sort())
        self.assertEqual("SPECIAL", Box(150, 100, 100, 10).sort())
        self.assertEqual("SPECIAL", Box(100, 150, 100, 10).sort())
        self.assertEqual("SPECIAL", Box(100, 100, 150, 10).sort())
    
    def test_rejected_box(self):
        box = Box(100, 100, 100, 100)
        self.assertEqual("REJECTED", box.sort())

    def test_is_bulky(self):
        self.assertTrue(Box(100, 100, 100, 10)._check_bulky())
        self.assertFalse(Box(100, 100, 10, 10)._check_bulky())

    def test_instance_exception(self):
        self.assertRaises(Exception, Box, ("", 100, 100, 10))
        self.assertRaises(Exception, Box, (100, "", 100, 10))
        self.assertRaises(Exception, Box, (100, 100, "", 10))
        self.assertRaises(Exception, Box, (100, 100, 10, ""))