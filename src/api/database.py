import os
import json
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
        self.db = firestore.client()
        self.orders_ref = self.db.collection('orders')
        self.food_ref = self.db.document('orders/foods')
        self.drinks_ref = self.db.document('orders/drinks')
        self.snacks_ref = self.db.document('orders/snacks')

    def put_food(self, incoming_json):
        currentFoodListKV = self._get_collection_data('foods')
        currentFoodListKeys = [key for key in currentFoodListKV]
        print(currentFoodListKeys)

        for food in incoming_json:
            print(food)
        # Update use to create new entries & update the already existing.
        self.food_ref.update(incoming_json)
        # pass

    def put_drinks(self):
        pass

    def put_snacks(self):
        pass

    def _get_collection_data(self, document):
        dbOrderCollection = self.db.collection('orders').get()
        if document == "foods":
            return dbOrderCollection[0].to_dict()
        elif document == "drinks":
            dbOrderCollection[1].to_dict()
        elif document == "snacks":
            dbOrderCollection[2].to_dict()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass