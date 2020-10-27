import os
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

dirname = os.path.dirname(__file__)

dbAuthKey = os.path.join(dirname, 'auth/key.json')
cred = credentials.Certificate(dbAuthKey)
firebase_admin.initialize_app(cred)

class DBHandler:
    def __enter__(self):
        pass

    def __init__(self):
        #Create DB if it does not exist (This is part of FTS for new modules)
        db = firestore.client()
        food_ref = db.collection('foods')
        drinks_ref = db.collection('drinks')
        snacks_ref = db.collection('snacks')



    def __exit__(self, exc_type, exc_val, exc_tb):
        pass