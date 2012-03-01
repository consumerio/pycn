# -*- coding: utf-8 -*-

"""
cn_client.tests
~~~~~~~~~~~~~~~~~~~

Tests of the ConsumerNotebook client API
"""
import ConfigParser
import json
import unittest

from functions import get_products, get_grids, get_lists, get_users
from functions import post_follow, post_unfollow

config = ConfigParser.ConfigParser()
config.read('tests.cfg')

API_KEY = config.get('Params', 'api_key')
USERNAME = config.get('Params', 'username')
PASSWORD = config.get('Params', 'password')
BASE_URL = config.get("Params", 'base_url')

def _lprint(response):
    """ Used to save html responses to help debug"""
    f = open('results.html','w')
    f.write(response.content)
    f.close()

class TestFunctions(unittest.TestCase):
    
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

    def test_lots(self):
        response = get_lists(API_KEY, USERNAME, PASSWORD, base_url=BASE_URL)
        self.assertEquals(response.status_code, 200)

    def test_grids(self):

        # Let's get a list of products
        response = get_grids(API_KEY, USERNAME, PASSWORD, base_url=BASE_URL)
        self.assertEquals(response.status_code, 200)
        
        response = get_grids(API_KEY, USERNAME, PASSWORD, base_url=BASE_URL, depth=1)

    def test_users(self):

        response = get_users(API_KEY, USERNAME, PASSWORD, target_username="audreyr", base_url=BASE_URL)        
        self.assertEquals(response.status_code, 200)

    def test_unfollow(self):
        response = post_unfollow(API_KEY, USERNAME, PASSWORD, target_username="audreyr", base_url=BASE_URL)        
        self.assertEquals(response.status_code, 202)
        
    def test_follow(self):
        # this line makes sure we are not following audreyr
        response = post_unfollow(API_KEY, USERNAME, PASSWORD, target_username="audreyr", base_url=BASE_URL)                
        
        # Follow audreyr
        response = post_follow(API_KEY, USERNAME, PASSWORD, target_username="audreyr", base_url=BASE_URL)        
        self.assertEquals(response.status_code, 201)

        # Follow audreyr and get a 400 because we are already doing so
        response = post_follow(API_KEY, USERNAME, PASSWORD, target_username="audreyr", base_url=BASE_URL)        
        self.assertEquals(response.status_code, 400)



if __name__ == "__main__":
    unittest.main()