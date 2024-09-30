import unittest
from g import some_function  # Assuming some_function is in g.py

class TestG(unittest.TestCase):
    def test_some_function(self):
        self.assertEqual(some_function(5), 25)  # Replace with your logic

if __name__ == '__main__':
    unittest.main()
