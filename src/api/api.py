import os
import json
from flask import Flask, escape, request, jsonify

import database

# A reference for relative path for this file to ensure that we're at the correct directory
dirname = os.path.dirname(__file__)

app = Flask(__name__)

with database.DBHandler() as db:
    # Revert debug when development is done

    @app.route('/')
    def hello():
        return {'products' : ['Food', 'Drinks', 'Snacks']}

    @app.route('/putOrder', methods=['PUT'])
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

        # Send request to drinks / kitchen
        db.put_food()
        db.put_drinks()
        db.put_snacks()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)