import unittest
import json
from app import app
from app.views import order_model
import os



class OrderstestCase(unittest.TestCase):

    def setUp(self):
        """
        will be called before every test
        """
        self.client = app.test_client
        self.user = {"username": "mwas", "password": "123",
                     "first_name": "kelvin", "last_name": "mwas"}

        self.logins = {"username": "mwas", "password": "123"}

        self.order = {
              "title": "snacks",
              "description": "Full chips and ketchup"
              }
        self.empty_order = {"title": "", "description": ""}
                              
       
        self.client().post('/api/v1/register', data=json.dumps(self.user),
                           content_type='application/json')

        self.login = self.client().post('/api/v1/login', data=json.dumps(self.logins),
                                        content_type='application/json')
                                        
     
    def tearDown(self):
        """ clear data after every test"""
        order_model.orders.clear()

    

    def test_order_can_create_successfully(self):
        """Tests that an order can be created successfully"""
        initial_count = len(order_model.orders)
        res = self.client().post('/api/v1/orders', data=json.dumps(self.order),
                                 headers={"content-type": "application/json"})
        final_count = len(order_model.orders)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(final_count - initial_count, 1)
        self.assertIn("Order created",str(res.data))
    
    def test_cannot_create_duplicate(self):
        """Tests that no two orders can exist with similar title"""
        title1 = self.client().post('/api/v1/orders',
                    headers={
                        "content-type": "application/json"})
                    
        title2 = self.client().post('/api/v1/orders',
                                  headers={"content-type": "application/json"})
        self.assertEqual(title2.status_code, 401)
        
        self.assertIn("Sorry, data already exists",str(title2.data))

    def test_cannot_create_with_name_only(self):
        """Tests that request title and description must be provided to create an new order"""
        res = self.client().post('/api/v1/orders', data=json.dumps(self.empty_order),
                                 headers={"content-type": "application/json"})
        
        self.assertIn("Name cannot be empty!",str(res.data))

    
    