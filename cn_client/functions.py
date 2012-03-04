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

def get_products(apikey, username=None, base_url="https://consumernotebook.com/api/v1/"):
    """ 
        Returns a requests response object containing a list of serialized
        Consumer Notebook product data.
    """
    data = {}
    data['apikey'] = apikey
    if username:
        data['username'] = target_username    
    url = base_url + 'products/'
    return requests.get(url, params=data)

def get_lists(apikey, username=None, base_url="https://consumernotebook.com/api/v1/"):
    """ 
        Returns a requests response object containing a list of serialized
        Consumer Notebook list data.
    """
    
    data = {}
    data['apikey'] = apikey       
    if username:
        data['username'] = username    
    url = base_url + 'lists/'        
    return requests.get(url, params=data)

def get_users(apikey, username=None, base_url="https://consumernotebook.com/api/v1/"):
    """ 
        Returns a requests response object containing a list of serialized
        Consumer Notebook user data.
    """
    data = {}
    data['apikey'] = apikey       
    if username:
        data['username'] = username
    url = base_url + 'users/'    
    return requests.get(url, params=data)