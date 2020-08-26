import unittest
from Controllers.Main import *
from Models.SearchRoute import *

#Variaveis de Teste
originOk = "MAO"
originNull = None
originEmpty = ""
destinyOk = "REC"
destinyNull = None
destinyEmpty = ""
amountOk = 358
amountZero = 0
amountNegative = -3
routeOk = "GRU-CDG"
routeWrong = "MAO-GRU"

class Route(unittest.TestCase):
    
    def test_validateCreateRouteOk(self):
        api = Main('input-file.csv')
        api.openningFile()
        self.assertTrue(api.dataFile.writeFile(originOk, destinyOk, amountOk))
    
    def test_validateCreateRouteOriginNull(self):
        api = Main('input-file.csv')
        api.openningFile()
        self.assertFalse(api.dataFile.writeFile(originNull, destinyOk, amountOk))

    def test_validateCreateRouteOriginEmpty(self):
        api = Main('input-file.csv')
        api.openningFile()
        self.assertFalse(api.dataFile.writeFile(originEmpty, destinyOk, amountOk))

    def test_validateCreateRouteDestinyNull(self):
        api = Main('input-file.csv')
        api.openningFile()
        self.assertFalse(api.dataFile.writeFile(originNull, destinyNull, amountOk))

    def test_validateCreateRouteDestinyEmpty(self):
        api = Main('input-file.csv')
        api.openningFile()
        self.assertFalse(api.dataFile.writeFile(originEmpty, destinyEmpty, amountOk))

    def test_validateCreateRouteAmountZero(self):
        api = Main('input-file.csv')
        api.openningFile()
        self.assertFalse(api.dataFile.writeFile(originNull, destinyOk, amountZero))

    def test_validateCreateRouteAmountNegative(self):
        api = Main('input-file.csv')
        api.openningFile()
        self.assertFalse(api.dataFile.writeFile(originEmpty, destinyEmpty, amountNegative))

    def test_SearchBetterRoute(self):
        api = Main('input-file.csv')
        api.openningFile()
        search = Search()
        self.assertEqual(['GRU-BRC-SCL-ORL-CDG', 40],
            search.better_price_travel(route=routeOk,dataRoutes= api.dataFile.dataInput))

    def test_SearchBetterRouteWrong(self):
        api = Main('input-file.csv')
        api.openningFile()
        search = Search()
        self.assertEqual(None,
            search.better_price_travel(route=routeWrong,dataRoutes= api.dataFile.dataInput))


    

if __name__ == '__main__':
    unittest.main()
    

