import uuid

class User(object):
   
   def __init__(self):
       self.users={}
       self.user_token={}

   def add_user(self,username,password,first_name,last_name):
       """
       creates a new user and appends to the list
       """
       data={"id":uuid.uuid4(),"username":username, "password":password,
             "first_name":first_name,"last_name":last_name}
       self.users[username] = data
       return self.users[username]

class Orders(object):
    """order model to store all order data"""
    def __init__(self):
        self.orders = {}

    def add_orders(self, title, description, user_id):
        """Adds a new order to the orders dictionary"""
        id=str(len(self.orders)+1)
        new_order = {
              "id" : id,
              "title": title,
              "description": description,
              "user_id": user_id
        }
        self.orders[id] = new_order
        return self.orders[id]