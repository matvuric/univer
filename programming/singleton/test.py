import unittest
from main import CurrenciesList


class TestPrecisionFunc(unittest.TestCase):
    def test_result_type(self):
        self.assertIsInstance(CurrenciesList(), type(CurrenciesList()))

    def test_is_singleton(self):
        my_cur_list = CurrenciesList()
        my_cur_list2 = CurrenciesList()
        my_cur_list2.get_currencies(["R01090B", "R01720", "R01565"])

        self.assertEqual(id(my_cur_list), id(my_cur_list2))


if __name__ == '__main__':
    unittest.main(verbosity=1)
