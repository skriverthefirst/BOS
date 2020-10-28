import os
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

# To ensure that we have the correct path
dirname = os.path.dirname(__file__)

# Initialize firebase_admin SDK
dbAuthKey = os.path.join(dirname, 'auth/key.json')
cred = credentials.Certificate(dbAuthKey)
firebase_admin.initialize_app(cred, {"projectId": "bestillingsorganiseringssystem"})


class DBHandler:
    '''
        DBHandler is made to control all incoming and outgoing database calls
    '''
    def __enter__(self):
        return DBHandler()

    def __init__(self):
        db = firestore.client()
        db.collection('orders')
        self.food_ref = db.document('orders/foods')
        self.drinks_ref = db.document('orders/drinks')
        self.snacks_ref = db.document('orders/snacks')

    def put_food(self):
        self.food_ref.update({'Food': '3'})

    def put_drinks(self):
        pass

    def put_snacks(self):
        pass


    def __exit__(self, exc_type, exc_val, exc_tb):
        pass