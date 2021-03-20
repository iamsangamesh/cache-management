import unittest 
from cache import Cache
  
class ResponsorCacheTest(unittest.TestCase): 

    def setUp(self): 
        self.responsor = Cache("test_files/responsor_test.json")
        self.responsor.clear()
        self.responsor.put("are you harshi","yes i am harshi")
  
    def test_whenValuePresent(self):         
        self.assertIsNotNone(self.responsor.get("are you harshi"))
        self.assertEqual(self.responsor.get("are you harshi"),"yes i am harshi") 

    def test_whenValueNotPresent(self):         
        self.assertIsNone(self.responsor.get("not present")) 

    def test_keys(self):         
        self.assertEqual(["are you harshi"],self.responsor.keys()) 
  
if __name__ == '__main__': 
    unittest.main() 