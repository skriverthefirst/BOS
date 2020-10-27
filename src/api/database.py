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
        pass

    def __init__(self):
        db = firestore.client()
        food_ref = db.collection('foods')
        drinks_ref = db.collection('drinks')
        snacks_ref = db.collection('snacks')

    def put_food():
        pass

    def put_drinks():
        pass

    def put_snacks():
        pass


    def __exit__(self, exc_type, exc_val, exc_tb):
        pass