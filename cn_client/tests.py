# -*- coding: utf-8 -*-

"""
cn_client.tests
~~~~~~~~~~~~~~~~~~~

Tests of the ConsumerNotebook client API
"""
import ConfigParser
import json
import unittest

from functions import get_products, get_lists, get_users

config = ConfigParser.ConfigParser()
config.read('tests.cfg')

API_KEY = config.get('Params', 'api_key')
BASE_URL = config.get("Params", 'base_url')

def lprint(response):
    """ Used to save html responses to help debug"""
    f = open('results.html','w')
    f.write(response.content)
    f.close()

class TestFunctions(unittest.TestCase):
        
        

    def test_https(self):
        
        # Let's get a list of products
        response = get_products(API_KEY, base_url="http://consumernotebook.com/api/v1/")
        self.assertEquals(response.status_code, 200)
        
        # We should just have one page
        response = get_products(API_KEY)
        self.assertEquals(response.status_code, 200)

    """
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
    """


if __name__ == "__main__":
    unittest.main()