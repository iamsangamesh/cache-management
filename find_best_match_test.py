import unittest 
from cache import Cache
from find_best_match import getBestMatch
  
class FindBestMatchTest(unittest.TestCase):
    def setUp(self): 
        self.responsor = Cache("test_files/responsor_best_match_test.json")
        self.responsor.clear()
        self.responsor.put("are you harshi","yes i am harshi")
        self.responsor.put("where is canteen","opposite to ground")
        self.responsor.put("can i buy juice in canteen","yes you can")

    def test_getBestMatch(self):         
        self.assertEqual("where is canteen",getBestMatch(self.responsor.keys(),"how can i go to canteen"))
    
    def test_getBestMatch_None(self):         
        self.assertEqual(None,getBestMatch(self.responsor.keys(),"what the hell"))

if __name__ == '__main__': 
    unittest.main() 