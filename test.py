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


    

if __name__ == '__main__':
    unittest.main()
    

