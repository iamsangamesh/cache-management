import unittest 
from cache import Cache
  
class TranslatorCacheTest(unittest.TestCase): 

    def setUp(self): 
        self.translator = Cache("translator.json")
        self.translator.clear()
  
    def test_whenValuePresent(self):         
        self.translator.put("welcome to home","welcome home to")
        self.assertIsNotNone(self.translator.get("welcome to home"))
        self.assertEqual(self.translator.get("welcome to home"),"welcome home to") 

    def test_whenValueNotPresent(self):         
        self.assertIsNone(self.translator.get("not present")) 
  
if __name__ == '__main__': 
    unittest.main() 