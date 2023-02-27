import unittest 
from flip import flip

class TestFlip(unittest.TestCase):
    def test_flip1(self):
        self.assertEqual(flip('ab'), 'ba')
    
    def test_add2(self):
        self.assertEqual(flip('a'), 'b')

# TestAdd().test_add()