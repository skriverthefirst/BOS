import unittest
from database import DBHandler

class test_database(unittest.TestCase):
    def setUp(self):
        self.db = DBHandler()

    # Successful json: {'Food': {'FoodNrOne': 2, 'FoodNrTwo': 2, 'FoodNrThree': 2, 'FoodNrFour': 2}}
    def test_put_food_empty_list(self):
        json = []
        res = self.db.put_food(json)
        self.assertFalse(res)

    def test_put_drinks_empty_list(self):
        json = []
        res = self.db.put_drinks(json)
        self.assertFalse(res)

    def test_put_snacks_empty_list(self):
        json = []
        res = self.db.put_snacks(json)
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()