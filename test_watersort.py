import unittest
from watersort import Bottle

class TestBottle(unittest.TestCase):
    
    def setUp(self):
        self.bottles = [Bottle() for _ in range(3)]
        
    def test_push(self):
        self.bottles[0].push('red')
        self.bottles[0].push('white')
        self.bottles[0].push('pink')
        self.bottles[0].push(None)
        
        self.bottles[1].push('white')
        self.bottles[1].push('white')
        self.bottles[1].push('red')
        self.bottles[1].push(None)
        
        self.bottles[2].push('red')
        self.bottles[2].push('pink')
        self.bottles[2].push(None)
        self.bottles[2].push(None)
        
        self.assertEqual(self.bottles[0].items, ['red', 'white', 'pink', None])
        self.assertEqual(self.bottles[1].items, ['white', 'white', 'red', None])
        self.assertEqual(self.bottles[2].items, ['red', 'pink', None, None])
        

if __name__ == "__main__":
    unittest.main()