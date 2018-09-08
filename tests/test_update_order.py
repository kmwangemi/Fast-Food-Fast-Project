import unittest
import json
from app import app
from app.views import order_model
#import os

class CreateUpadateOrderTestCase(unittest.TestCase):
    """This class represents the api test case"""

    def setUp(self):
        """
        Will be called before every test
        """
        self.client = app.test_client
        self.user = {
            "username": "mwas",
            "password": "123",
            "first_name": "kelvin",
            "last_name": "mwas"
        }

        self.logins = {"username": "mwas", "password": "123"}

        self.order = {
              "title": "snacks",
              "description": "Full chips and ketchup"
              }
        self.update_order = {
            "title": "",
            "description": ""
        }
        self.client().post(
            '/api/v1/register',
            data=json.dumps(self.user),
            content_type='application/json'
        )
        '''
        self.login = self.client().post(
            '/api/v1/login',
            data=json.dumps(self.logins),
            content_type='application/json'
        )
        self.data = json.loads(self.login.get_data(as_text=True))
        # get the token to be used by tests
        self.token = self.data['auth_token']
        '''
    def tearDown(self): 
        """ clear data after every test"""

    def test_order_can_be_updated_successfully(self):
        """Tests that an order can be updated successfully"""
        order_model.orders.clear()
        res = self.client().post('/api/v1/orders', data=json.dumps(self.order),
                                 headers={"content-type": "application/json"})
                                         
        res2 = self.client().put('/api/v1/orders/1', data=json.dumps(self.update_order),
                                 headers={"content-type": "application/json", })
                                          
        self.assertEqual(res2.status_code, 202)
        self.assertIn("order updated!",str(res2.data))

    def test_can_get_order(self):
        """test can get all orders"""
        order_model.orders.clear()
        self.client().post('/api/v1/orders', data=json.dumps(self.order),
                           headers={"content-type": "application/json"})
                                    
        res = self.client().get('/api/v1/orders')
                                
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(order_model.orders), 1)

  
        
        
 