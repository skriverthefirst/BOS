import os
import json
from flask import Flask, escape, request, jsonify

import database

# A reference for relative path for this file to ensure that we're at the correct directory
dirname = os.path.dirname(__file__)

with database.DBHandler() as db:
    app = Flask(__name__)

    # Routes for the REST API
    @app.route('/')
    def hello():
        return f'Hello, world!'

    # GET

    # POST

    # PUT

    # DELETE