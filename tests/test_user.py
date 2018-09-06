"""Module contains unittest for the User class"""
import unittest


class TestUser(unittest.TestCase):
    """Tests for methods in the user"""

    def setUp(self):
        """Setting up a user to use for each test"""
        self.myuser = User('kelvin',
                           'mwas',
                           'mwas',
                           '123',
                           'mwas@gmail.com')

    def test_create_order_success(self):
        """Testing whether an order was successfully created,
        it should increase the length of self.orderlists"""
        count_before = len(self.myuser.orders)
        self.myuser.create_order('Snacks',
                                      'Full chips and ketchup')
        count_after = len(self.myuser.orders)
        self.assertEqual(count_after, count_before + 1,
                         msg='orders should increase by one')

    def test_create_orderlist_non_string_input(self):
        """Method should raise a type error for non string inputs"""
        self.assertRaises(TypeError,
                          self.myuser.create_order,
                          '50 chips', 50,
                          msg="Method only accept string inputs")

    def test_view_orderlists_success(self):
        """View_orderlists should return a list"""
        orderlists = self.myuser.view_orders()
        self.assertIsInstance(orderlists, list)

if __name__ == '__main__':
    unittest.main()
