import os
from firebase_admin import credentials, firestore, initialize_app

dirname = os.path.dirname(__file__)

dbAuthKey = os.path.join(dirname, 'auth/key.json')
cred = credentials.Certificate(dbAuthKey)
firebase_admin.initialize_app(cred)

class DBHandler:
    def __init__():
        db = firestore.client()
        food_ref = db.collection('foods')
        drinks_ref = db.collection('drinks')
        snacks_ref = db.collection('snacks')