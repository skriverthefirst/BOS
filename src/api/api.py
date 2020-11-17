import os
import json
from flask import Flask, escape, request, jsonify

import database

# A reference for relative path for this file to ensure that we're at the correct directory
dirname = os.path.dirname(__file__)

app = Flask(__name__)

with database.DBHandler() as db:

    orders = []

    @app.route('/', methods=['GET'])
    def root():
        return jsonify({"Success": True}), 200

    @app.route('/putOrder', methods=['POST'])
    def put_order():
        '''
            Orders should come in as followes:
            [
                {
                    "Food" : {
                        "FoodNrOne":2,
                        "FoodNrTwo":2,
                        "FoodNrThree":2,
                        "FoodNrFour": 2
                    }
                },
                {
                    "Drinks" : {
                        "DrinkNrOne" : {"Amount" : 2, "Size": 1},
                        "DrinkNrTwo" : {"Amount" : 2, "Size": 2},
                        "DrinkNrThree" : {"Amount" : 2, "Size": 3}
                    }
                },
                {
                    "Snacks" : {
                        "SnackNrOne" : {"Amount" : 2, "Size": 1},
                        "SnackNrTwo" : {"Amount" : 2, "Size": 2},
                        "SnackNrThree" : {"Amount" : 2, "Size": 3}
                    }
                }
            ]
        '''
        incomingJson = request.get_json(force=True)

        food = incomingJson[0] if len(incomingJson) > 0 and "Food" in incomingJson[0] else []
        drinks = incomingJson[1] if len(incomingJson) > 1 and "Drinks" in incomingJson[1] else []
        snacks = incomingJson[2] if len(incomingJson) > 2 and "Snacks" in incomingJson[2] else []

        orders.append(food)

        print(f"FOOD! {food}")
        print(f"DRINKS! {drinks}")
        print(f"SNACKS! {snacks}")

        #     # Send request to drinks / kitchen
        #     # db.put_food(food)
        return jsonify({"Success": True}), 200

    @app.route("/getOrder", methods=['GET'])
    def get_order():
        if not orders:
            return jsonify({"List is empty": False}), 202
        else:
            orders.clear()
            return jsonify({"Sucess": True}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)