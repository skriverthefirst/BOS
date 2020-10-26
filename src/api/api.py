import os
from flask import Flask, escape, request
from firebase_admin import credentials, firestore, initialize_app

# A reference for relative path for this file to ensure that we're at the correct directory
dirname = os.path.dirname(__file__)

dbAuthKey = os.path.join(dirname, 'auth/key.json')
cred = credentials.Certificate(dbAuthKey)

# Initialization of essentials
firebase_admin.initialize_app(cred)
db = firestore.client()
app = Flask(__name__)

# Routes for the REST API

@app.route('/')
def hello():
    return f'Hello, world!'

# GET

# POST

# PUT

# DELETE