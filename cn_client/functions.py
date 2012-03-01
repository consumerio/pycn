# -*- coding: utf-8 -*-

"""
cn_client.functions
~~~~~~~~~~~~~~~~~~~

This module provides a basic API interface for Consumer Notebook. The 
abstraction of this is super-light in order to show how to use the API.

All Functions return a python-requests response object. It is up to the
user of this API to convert that to Python data
"""

import requests

def get_products(api_key, username, password, target_username=None, page=1,from_date=None, to_date=None, base_url="https://consumernotebook.com/api/v1/"):
    """ 
        Returns a requests response object containing a list of serialized
        Consumer Notebook product data.
    """
    data = {}
    data['api_key'] = api_key    
    data['page'] = page
    data['from_date'] = from_date
    data['to_date'] = to_date
    if target_username:
        data['username'] = target_username    
    url = base_url + 'products.json'
    return requests.get(url, auth=(username, password), data=data)

def get_lists(api_key, username, password, target_username=None, page=1,from_date=None, to_date=None, depth=0, base_url="https://consumernotebook.com/api/v1/"):
    """ 
        Returns a requests response object containing a list of serialized
        Consumer Notebook list data.
    """
    data = {}
    data['api_key'] = api_key       
    data['page'] = page
    data['from_date'] = from_date
    data['to_date'] = to_date
    data['depth'] = depth    
    if target_username:
        data['username'] = target_username    
    url = base_url + 'lists.json'    
    return requests.get(url, auth=(username, password), data=data)

def get_grids(api_key, username, password, target_username=None, page=1,from_date=None, to_date=None, depth=0, base_url="https://consumernotebook.com/api/v1/"):
    """ 
        Returns a requests response object containing a list of serialized
        Consumer Notebook grid data.
    """
    data = {}
    data['api_key'] = api_key       
    data['page'] = page
    data['from_date'] = from_date
    data['to_date'] = to_date
    data['depth'] = depth    
    if target_username:
        data['username'] = target_username    
    url = base_url + 'grids.json'    
    return requests.get(url, auth=(username, password), data=data)

def get_users(api_key, username, password, target_username=None, page=1,base_url="https://consumernotebook.com/api/v1/"):
    """ 
        Returns a requests response object containing a list of serialized
        Consumer Notebook grid data.
    """
    data = {}
    data['api_key'] = api_key       
    data['page'] = page
    data['from_date'] = from_date
    data['to_date'] = to_date
    data['depth'] = depth 
    if target_username:
        data['username'] = target_username
    url = base_url + 'grids.json'    
    return requests.get(url, auth=(username, password), data=data)
