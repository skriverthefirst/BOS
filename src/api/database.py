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

    def put_food(self, incomingJson):
        dbFoodListK, dbFoodListV, inJsonK, inJsonV = self._extract_keys_values(incomingJson, 'foods', 'Food')

        for index, food in enumerate(inJsonK):
            if food in dbFoodListK:
                incomingJson['Food'][food] = dbFoodListV[index] + inJsonV[index]

        self.food_ref.update(incomingJson)

    def put_drinks(self, incomingJson):
        dbDrinkListK, dbDrinkListV, inJsonK, inJsonV = self._extract_keys_values(incomingJson, 'drinks', 'Drink')

        for index, drink in enumerate(inJsonK):
            if drink in dbDrinkListK:
                incomingJson['Drink'][drink] = dbDrinkListV[index] + inJsonV[index]

        self.food_ref.update(incomingJson)

    def put_snacks(self, incomingJson):
        dbSnackListK, dbSnackListV, inJsonK, inJsonV = self._extract_keys_values(incomingJson, 'snacks', 'Snack')

        for index, food in enumerate(inJsonK):
            if food in dbFoodListK:
                incomingJson['Snack'][snack] = dbSnackListV[index] + inJsonV[index]

        self.food_ref.update(incomingJson)

    def _get_document_data(self, document):
        if document == "foods":
            foods = self.food_ref.get().to_dict()
            return foods["Food"]
        elif document == "drinks":
            drinks = self.drinks_ref.get().to_dict()
            return drinks["Drinks"]
        elif document == "snacks":
            snacks = self.snacks_ref.get().to_dict()
            return snacks["Snacks"]

    def _extract_keys_values(self, incomingJson, document, subject):
        currentFoodListKV = self._get_document_data(document)
        currentFoodListKeys = [key for key in currentFoodListKV.keys()]
        currentFoodListValues = [value for value in currentFoodListKV.values()]
        incomingJsonKeys = [key for key in incomingJson.get(subject).keys()]
        incomingJsonValues = [key for key in incomingJson.get(subject).values()]
        return currentFoodListKeys, currentFoodListValues, incomingJsonKeys, incomingJsonValues

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass