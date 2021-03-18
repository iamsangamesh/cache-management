import unittest 
from cache import Cache
  
class RespondorCacheTest(unittest.TestCase): 

    def setUp(self): 
        self.respondor = Cache("respondor.json")
        self.respondor.clear()
  
    def test_whenValuePresent(self):         
        self.respondor.put("are you harshi","yes i am harshi")
        self.assertIsNotNone(self.respondor.get("are you harshi"))
        self.assertEqual(self.respondor.get("are you harshi"),"yes i am harshi") 

    def test_whenValueNotPresent(self):         
        self.assertIsNone(self.respondor.get("not present")) 
  
if __name__ == '__main__': 
    unittest.main() 