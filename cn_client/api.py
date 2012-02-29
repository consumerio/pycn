# -*- coding: utf-8 -*-

"""
cn_client.api
~~~~~~~~~~~~~

This module provides the basic API interface for Consumer Notebook.
"""

import json

import requests

CONSUMERNOTEBOOK_URL = 'https://consumernotebook.com/api/v1/'


class ConsumerNotebookCore(object):
    """The core ConsumerNotebook class."""
    def __init__(self):
        super(ConsumerNotebookCore, self).__init__()

        #: The User's API Key.
        self._api_key = None
        self._api_key_verified = None
        self._s = requests.session()
        self._cn_url = CONSUMERNOTEBOOK_URL

        # We only want JSON back.
        self._s.headers.update({'Accept': 'application/json'})

    def __repr__(self):
        return '<ccn-core at 0x%x>' % (id(self))

    def login(self, username, password):
        """Logs user into Consumer Notebook with given credentials."""

        # Attach auth to session.
        self._s.auth = (username.password)

        return True

    @property
    def is_authenticated(self):
        if self._api_key_verified is None:
            return self._verify_api_key()
        else:
            return self._api_key_verified

    def _url_for(self, *args):
        args = map(str, args)
        return '/'.join([self._cn_url] + list(args))

    @staticmethod
    def _resource_serialize(o):
        """Returns JSON serialization of given object."""
        return json.dumps(o)

    @staticmethod
    def _resource_deserialize(s):
        """Returns dict deserialization of a given JSON string."""

        try:
            return json.loads(s)
        except ValueError:
            raise ResponseError('The API Response was not valid.')

    def _http_resource(self, method, resource, params=None, data=None):
        """Makes an HTTP request."""

        if not is_collection(resource):
            resource = [resource]

        url = self._url_for(*resource)
        r = self._s.request(method, url, params=params, data=data)

        r.raise_for_status()

        return r

    def _get_resource(self, resource, obj, params=None, **kwargs):
        """Returns a mapped object from an HTTP resource."""
        r = self._http_resource('GET', resource, params=params)
        item = self._resource_deserialize(r.content)

        return obj.new_from_dict(item, h=self, **kwargs)

    def _get_resources(self, resource, obj, params=None, map=None, **kwargs):
        """Returns a list of mapped objects from an HTTP resource."""
        r = self._http_resource('GET', resource, params=params)
        d_items = self._resource_deserialize(r.content)

        items =  [obj.new_from_dict(item, h=self, **kwargs) for item in d_items]

        if map is None:
            map = KeyedListResource

        list_resource = map(items=items)
        list_resource._h = self
        list_resource._obj = obj

        return list_resource


class ConsumerNotebook(ConsumerNotebookCore):
    """The main ConsumerNotebook class."""

    def __init__(self):
        super(ConsumerNotebook, self).__init__()

    def __repr__(self):
        return '<github-client at 0x%x>' % (id(self))
        

class ResponseError(ValueError):
    """The API Response was unexpected."""