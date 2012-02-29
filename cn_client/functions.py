# -*- coding: utf-8 -*-

"""
cn_client.functions
~~~~~~~~~~~~~~~~~~~

This module provides the basic API interface for Consumer Notebook. The 
abstraction of this is super-light in order to show how to 
"""

import json

import requests

CONSUMERNOTEBOOK_URL = "https://api.consumernotebook.com/api/v1/"

def products(api_key, username, password, page=1,from_date=None, to_date=None):
    """ Returns a ``requests`` response object"""
    data = {}
    data['page'] = page
    data['from_date'] = from_date
    data['to_date'] = to_date
    url = CONSUMERNOTEBOOK_URL + 'products/'
    return request.get(url, auth=(username, password), data=data)

def lists(api_key, username, password, page=1,from_date=None, to_date=None, depth=0):
    """ Returns a ``requests`` response object"""
    data = {}
    data['page'] = page
    data['from_date'] = from_date
    data['to_date'] = to_date
    data['depth'] = depth    
    url = CONSUMERNOTEBOOK_URL + 'lists/'    
    return request.get(url, auth=(username, password), data=data)

def grids(api_key, username, password, page=1,from_date=None, to_date=None, depth=0):
    """ Returns a ``requests`` response object"""
    data = {}
    data['page'] = page
    data['from_date'] = from_date
    data['to_date'] = to_date
    data['depth'] = depth    
    url = CONSUMERNOTEBOOK_URL + 'grids/'    
    return request.get(url, auth=(username, password), data=data)
