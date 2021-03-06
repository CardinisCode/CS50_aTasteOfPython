import unittest
import cash_challenge


class TestCashValueGivenIsValid(unittest.TestCase):
    def testGivenEmptyVariableReturnErrorMessage(self):
        cash = ''
        message = "No value provided, please try again."
        self.assertEqual(cash_challenge.verify_change_is_valid(cash), message)
    
    def testGivenValueZeroReturnsErrorMessage(self):
        cash = 0
        message = "Please provide a value higher than 0."
        self.assertEqual(cash_challenge.verify_change_is_valid(cash), message)

    def testGivenStringInValueReturnErrorMessage(self):
        cash = "s"
        message = "Please provide integers or floats only"

        self.assertEqual(cash_challenge.verify_change_is_valid(cash), message)


class TestCashGivenReturnsCorrectMinimumChangeQuantity(unittest.TestCase):
    def testGivenOneUSCentReturns1coin(self):
        cash = 1

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 1)

    def test_given2Cent_returns2coins(self):
        cash = 2

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 2)

    def test_given3Cents_returns3coins(self):
        cash = 3

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 3)

    def test_given5cents_returns1coin(self):
        cash = 5

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 1) 

    def test_given10cents_returns1coin(self):
        cash = 10

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 1)

    def test_given20cents_returns2coins(self):
        cash = 20

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 2)

    def test_given6cents_returns2coins(self):
        cash = 6

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 2)

    def test_given7cents_returns3coins(self):
        cash = 7

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 3)  

    def test_given8cents_returns4coins(self):
        cash = 8

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 4)              

    def test_given11cents_returns2coins(self):
        cash = 11

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 2) 

    def test_given15cents_returns2coins(self):
        cash = 15

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 2)  

    def test_given21cents_returns3coins(self):
        cash = 21

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 3)                      

    def test_given22cents_returns4coins(self):
        cash = 22

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 4)  

    def test_given23cents_returns5coins(self):
        cash = 23

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 5)

    def test_given25cents_returns1coin(self):
        cash = 25

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 1)                       

    def test_given26cents_returns2coins(self):
        cash = 26

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 2) 

    def test_given27cents_returns3coins(self):
        cash = 27

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 3)  

    def test_given50cents_returns2coins(self):
        cash = 50

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 2)  

    def test_given51cents_returns3coins(self):
        cash = 51

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 3) 

    def test_given52cents_returns4coins(self):
        cash = 52

        actual = cash_challenge.check_cash_for_minimum_change(cash)

        self.assertEqual(actual, 4)                      



if __name__ == '__main__':
    unittest.main()