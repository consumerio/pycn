# -*- coding: utf-8 -*-

"""
cn_client.tests
~~~~~~~~~~~~~~~~~~~

Tests of the ConsumerNotebook client API
"""
import ConfigParser
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
        products = get_products(API_KEY, USERNAME, PASSWORD, base_url=BASE_URL)
        f = open('result.html','w')
        f.write(products.content)
        f.close()
        print products.content

if __name__ == "__main__":
    unittest.main()