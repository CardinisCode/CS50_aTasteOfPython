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





if __name__ == '__main__':
    unittest.main()