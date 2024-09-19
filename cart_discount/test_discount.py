import unittest 
from unittest import TestCase
from price_discount import discount  


class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))
    
    # TODO more unit tests here. Each test should test one scenario
    def test_list_of_under_three_prices(self):
        prices = []
        if len(prices) < 3:
            expected_discount = 0
            self.assertEqual(expected_discount, discount(prices))
        else:
            return

    def test_list_with_empty_list(self):
        prices = []
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))





if __name__ == '__main__':
    unittest.main()
