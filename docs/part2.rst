
.. _tutorial-part-2:

Part 2: Using the Users API
===========================

Now that you have the user's access token, you're ready to use any of the 
Consumer Notebook APIs.  

Let's start with getting the user's profile data via the Users API.

Get profile data
----------------

In this section, you'll learn how to make your first API call: `GET /api/v1/my-profile/ <http://api.consumernotebook.com/en/latest/api/v1/my-profile.html#api-v1-my-profile>`_.

Add the following code to your app::

    api = pycn.API(auth)
    profile = api.my_profile()

The `profile` object should now contain the user's profile data. 

You can access any of the profile fields as you would any Python object:

    * profile.username is the user's Consumer Notebook username
    * profile.followers is a Python list of the user's followers
    * profile.fullname is the user's full name
    * ...and so on.  

When using any of the API calls, consult the REST API docs for a full list of
available fields in the response object.
