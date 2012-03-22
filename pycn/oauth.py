import json
import requests

class AuthorizationURLError(Exception):
    pass

class AccessTokenError(Exception):
    pass

class OAuth2Handler(object):

    def __init__(self, client_id, client_secret, redirect_uri):
        """ Parameters:
                client_id: The client app ID (get this from the provider)
                client_secret: The client app secret (get this from the provider)
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.access_token = None
        
    def get_authorization_url(self):
        return "http://consumernotebook.com/oauth2/authorize?client_id={0}&response_type=code&redirect_uri={1}".format(
                self.client_id,
                self.redirect_uri
            )

    def get_access_token(self, code=None):
        # First, try the user's existing profile
        if self.access_token:
            return self.access_token

        # If there's no working access token, and if we have a code,
        # then retrieve a new access token
        if code:
            url = 'http://consumernotebook.com/oauth2/access_token/'
            params = {
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'grant_type': 'authorization_code',
                'redirect_uri': self.redirect_uri, 
                'code': code
            }

            r = requests.post(url, data=params)
            if r.status_code == 200:
                access_token_json = json.loads(r.content)
                self.access_token = access_token_json[u'access_token']
                return self.access_token
        return None