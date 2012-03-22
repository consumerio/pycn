
.. _tutorial-part-1:

Part 1: Authentication
======================

The Consumer Notebook API uses OAuth 2.0 for authentication.  pycn
tries to make this painless for you.

Setup
-----

In your app, create an OAuth2Handler somewhere convenient::

    import pycn

    auth = pycn.OAuth2Handler(
            client_id='your-client-id',
            client_secret='your-client-secret',
            redirect_uri='your-redirect-uri'
        )

Display a Connect button
------------------------

Put a "Connect with CN" link button on one of your pages.  Have it go to the
URL returned by `get_authorization_url()`::

    try:
        connect_url = auth.get_authorization_url()
    except pycn.AuthorizationURLError:
        print "Error! Failed to get authorization URL."

Your template will need to contain something like this::

    <a class="btn" href="{{ connect_url }}">Connect</a> with Consumer Notebook

User visits the Authorization page
----------------------------------

When the user clicks "Connect", they get sent to a page on consumernotebook.com
asking the user whether they want to allow your app to access their Consumer
Notebook account.

If they click "Allow", they get sent back to your app.  (This is what the 
redirect URI is for.)

Get an Access Token
-------------------

Once the user clicks "Allow", they get sent to the redirect page on your site,
with a `code=some-random-code` GET request parameter.

Your app should take the `code` value and use it to make a server-side call to
the Consumer Notebook API, requesting an access token::

    # Get the "code" value
    code = self.request.get('code')

    # Use it to get an access token
    try:
        access_token = auth.get_access_token(code)
    except pycn.AccessTokenError:
        print 'Error! Failed to get access token.'

Once you've gotten the access token, save it somewhere in the user's account
for future use.

Now, let's move on to :ref:`tutorial-part-2`.
