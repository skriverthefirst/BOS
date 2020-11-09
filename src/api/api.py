import os
import json
from flask import Flask, escape, request, jsonify

import database

# A reference for relative path for this file to ensure that we're at the correct directory
dirname = os.path.dirname(__file__)

app = Flask(__name__)

with database.DBHandler() as db:
    # Revert debug when development is done

    @app.route('/', methods=['GET'])
    def root():
        return jsonify({"Success": True}), 200

    @app.route('/putOrder', methods=['POST'])
    def put_order():
        '''
            Orders should come in as followes:
            {
                Food : [
                    "Food nr. 1" : "Amount",
                    "Food nr. 2" : "Amount",
                    "Food nr. 3" : "Amount",
                    ],
                Drinks : [
                    "Drink nr. 1" : ["Amount", "Size"],
                    "Drink nr. 2" : ["Amount", "Size"],
                    "Drink nr. 3" : ["Amount", "Size"],
                    ],
                Snacks : [
                    "Snack nr. 1" : ["Amount", "Size"],
                    "Snack nr. 2" : ["Amount", "Size"],
                    "Snack nr. 3" : ["Amount", "Size"],
                ]
            }
        '''
        incomingJson = request.get_json()

        if len(incomingJson) > 0:
            food = incomingJson[0] if "Food" in incomingJson[0] else []
            drinks = incomingJson[1] if "Drinks" in incomingJson[1] else []
            snacks = incomingJson[2] if "Snacks" in incomingJson[2] else []

            print(f"FOOD! {food}")
            print(f"DRINKS! {drinks}")
            print(f"SNACKS! {snacks}")

            # Send request to drinks / kitchen
            # db.put_food(food)
            # db.put_drinks()
            # db.put_snacks()
            return jsonify({"Success": True}), 200
        else:
            return jsonify({}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)