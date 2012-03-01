# -*- coding: utf-8 -*-

"""
cn_client.functions
~~~~~~~~~~~~~~~~~~~

This module provides the basic API interface for Consumer Notebook. The 
abstraction of this is super-light in order to show how to use the API.
"""

import json

import requests

def get_products(api_key, username, password, page=1,from_date=None, to_date=None, base_url="https://consumernotebook.com/api/v1/"):
    """ Returns a ``requests`` response object"""
    data = {}
    data['api_key'] = api_key    
    data['page'] = page
    data['from_date'] = from_date
    data['to_date'] = to_date
    url = base_url + 'products/'
    return requests.get(url, auth=(username, password), data=data)

def get_lists(api_key, username, password, page=1,from_date=None, to_date=None, depth=0, base_url="https://consumernotebook.com/api/v1/"):
    """ Returns a ``requests`` response object"""
    data = {}
    data['page'] = page
    data['from_date'] = from_date
    data['to_date'] = to_date
    data['depth'] = depth    
    url = base_url + 'lists/'    
    return requests.get(url, auth=(username, password), data=data)

def get_grids(api_key, username, password, page=1,from_date=None, to_date=None, depth=0, base_url="https://consumernotebook.com/api/v1/"):
    """ Returns a ``requests`` response object"""
    data = {}
    data['page'] = page
    data['from_date'] = from_date
    data['to_date'] = to_date
    data['depth'] = depth    
    url = base_url + 'grids/'    
    return requests.get(url, auth=(username, password), data=data)
