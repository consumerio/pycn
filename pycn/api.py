# -*- coding: utf-8 -*-

"""
cn_client.api
~~~~~~~~~~~~~

This module provides the basic API interface for Consumer Notebook. This
will demonstrate use of the requests session functionality.
"""

import json

import requests
from pycn import restconsumer

DOMAIN = "https://consumernotebook.com/api/v1/"

class API(object):
    
    def __init__(self, oauth):
        self.oauth = oauth
    
    def my_profile(self):
        url = "{0}my-profile/?access_token={1}".format(DOMAIN, self.oauth.access_token)
        r = requests.get(url)
        return json.loads(r.content)
        
        
    