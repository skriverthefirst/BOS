import urllib3
import json
import unittest
from flask import Flask
from flask_testing import TestCase

class TestRestServer(TestCase):

    def setUp(self):
        self.http = urllib3.PoolManager()

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_server_is_running(self):
        response = self.http.request('GET', "http://127.0.0.1:5000")
        self.assertEqual(response.status, 200)

    # def test_api_put_order(self):
    #     encoded_json = json.dumps([])
    #     response = self.http.urlopen('POST', "http://127.0.0.1:5000/putOrder", body={encoded_json})
    #     self.assertEqual(response.status, 200)

if __name__ == '__main__':
    unittest.main()