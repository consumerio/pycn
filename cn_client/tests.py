# -*- coding: utf-8 -*-

"""
cn_client.tests
~~~~~~~~~~~~~~~~~~~

Tests of the ConsumerNotebook client API
"""
import ConfigParser
import json
import unittest

from functions import get_products

config = ConfigParser.ConfigParser()
config.read('tests.cfg')

API_KEY = config.get('Params', 'api_key')
USERNAME = config.get('Params', 'username')
PASSWORD = config.get('Params', 'password')
BASE_URL = config.get("Params", 'base_url')

class TestProducts(unittest.TestCase):
    
    def test_authentication(self):
        
        # Fail on bad API key. Should return a 401
        response = get_products("I am crazy", USERNAME, PASSWORD, base_url=BASE_URL)
        self.assertEquals(response.status_code, 401)

        # Fail on bad Username/Password combo. Returns a 404 but the API needs to change that
        response = get_products(API_KEY, USERNAME, "My password is passw0rd", base_url=BASE_URL)
        self.assertEquals(response.status_code, 404)

        # Successful authentication
        response = get_products(API_KEY, USERNAME, PASSWORD, base_url=BASE_URL)
        self.assertEquals(response.status_code, 200)
        
    def test_products(self):
        
        # Let's get a list of products
        response = get_products(API_KEY, USERNAME, PASSWORD, base_url=BASE_URL)
        self.assertEquals(response.status_code, 200)
        
        # We should just have one page
        products = json.loads(response.content)
        self.assertEquals(len(products), 20)

if __name__ == "__main__":
    unittest.main()