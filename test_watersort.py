import unittest
from watersort import Bottle, pour

class TestBottleArray(unittest.TestCase):
    
    def setUp(self):
        self.bottles = [Bottle() for _ in range(5)]
    
    
    def test_empty_bottles(self):
        """Test that newly created bottles are empty."""
        for bottle in self.bottles:
            self.assertTrue(bottle.is_empty())
    
    
                
    def test_push(self):
        self.assertTrue(self.bottles[0].is_empty())
        self.assertTrue(self.bottles[1].is_empty())
        self.assertTrue(self.bottles[2].is_empty())
        
        self.bottles[0].push('blue')
        self.bottles[0].push('blue')
        self.bottles[0].push('blue')
        self.bottles[0].push('blue')
        
        self.bottles[1].push('green')
        self.bottles[1].push('white')
        self.bottles[1].push('black')
        self.bottles[1].push(None)
        
        self.bottles[2].push('yellow')
        self.bottles[2].push('pink')
        self.bottles[2].push('green')
        self.bottles[2].push('orange')
        
        self.assertEqual(self.bottles[0].items, ['blue', 'blue', 'blue', 'blue'])
        self.assertEqual(self.bottles[1].items, ['green', 'white', 'black', None])
        self.assertEqual(self.bottles[2].items, ['yellow', 'pink', 'green', 'orange'])
        
        self.assertTrue(self.bottles[0].is_full())
        self.assertTrue(self.bottles[1].is_full())
        self.assertTrue(self.bottles[2].is_full())
        
        self.assertEqual(self.bottles[0].is_sorted(), True)
        self.assertEqual(self.bottles[1].is_sorted(), False)
        self.assertEqual(self.bottles[2].is_sorted(), False)
    
    
    
    def test_pour(self):
        self.bottles[0].push('yellow')
        self.bottles[0].push('yellow')
        self.bottles[0].push('blue')
        self.bottles[0].push('blue')
        
        self.bottles[1].push('blue')
        self.bottles[1].push('red')
        self.bottles[1].push('yellow')
        self.bottles[1].push('yellow')
        
        self.bottles[2].push('red')
        self.bottles[2].push('red')
        self.bottles[2].push('red')
        self.bottles[2].push('blue')
        
        self.bottles[3] = Bottle()
        
        self.assertEqual(self.bottles[0].items, ['yellow', 'yellow', 'blue', 'blue'])
        self.assertEqual(self.bottles[1].items, ['blue', 'red', 'yellow', 'yellow'])
        self.assertEqual(self.bottles[2].items, ['red', 'red', 'red', 'blue'])
        self.assertEqual(self.bottles[3].items, [None, None, None, None])
        
        pour(self.bottles[0], self.bottles[3])
        
        self.assertEqual(self.bottles[0].items, ['yellow', 'yellow', None, None])
        self.assertEqual(self.bottles[1].items, ['blue', 'red', 'yellow', 'yellow'])
        self.assertEqual(self.bottles[2].items, ['red', 'red', 'red', 'blue'])
        self.assertEqual(self.bottles[3].items, ['blue', 'blue', None, None])
        
        pour(self.bottles[2], self.bottles[3])
        
        self.assertEqual(self.bottles[2].items, ['red', 'red', 'red', None])
        self.assertEqual(self.bottles[3].items, ['blue', 'blue', 'blue', None])
        
        pour(self.bottles[1], self.bottles[0])
        
        self.assertEqual(self.bottles[0].items, ['yellow', 'yellow', 'yellow', 'yellow'])
        self.assertEqual(self.bottles[1].items, ['blue', 'red', None, None])
        
        pour(self.bottles[1], self.bottles[2])
        
        self.assertEqual(self.bottles[1].items, ['blue', None, None, None])
        self.assertEqual(self.bottles[2].items, ['red', 'red', 'red', 'red'])
        
        pour(self.bottles[1], self.bottles[3])
        
        self.assertEqual(self.bottles[0].items, ['yellow', 'yellow', 'yellow', 'yellow'])
        self.assertEqual(self.bottles[1].items, [None, None, None, None])
        self.assertEqual(self.bottles[2].items, ['red', 'red', 'red', 'red'])
        self.assertEqual(self.bottles[3].items, ['blue', 'blue', 'blue', 'blue'])
        
        self.assertEqual(self.bottles[0].is_sorted(), True)
        self.assertEqual(self.bottles[1].is_sorted(), True)
        self.assertEqual(self.bottles[2].is_sorted(), True)
        self.assertEqual(self.bottles[3].is_sorted(), True)
        
        
        
if __name__ == "__main__":
    unittest.main()