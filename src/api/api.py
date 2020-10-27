import os
import json
from flask import Flask, escape, request, jsonify

import database

# A reference for relative path for this file to ensure that we're at the correct directory
dirname = os.path.dirname(__file__)

with database.DBHandler() as db:
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return f'Hello, world!'

    # PUT
    @app.route('/putFood', methods=['PUT'])
    def put_food():
        # Send request to drinks / kitchen
        db.put_food()

    @app.route('/putDrinks', methods=['PUT'])
    def put_drinks():
        # Send request to drinks / kitchen
        db.put_drinks()

    @app.route('/putSnacks', methods=['PUT'])
    def put_snacks():
        # Send request to drinks / kitchen
        db.put_snacks()

    # DELETE