Authentication
==============

Authentication is performed using OAuth2 protocol. The implementation is based on
`django-oauth2-providers <https://django-oauth2-provider.readthedocs.io/en/latest/>`_ Django application so for generale
documentation overview refer to the official documentation. Here we only explain the difference of the MOST implementation.

MOST implementation requires also the *taskgroup* field to get an access_token in the REST call.

REST API
********

.. http:post:: /oauth2/access_token/

    It authenticates the client providing an access token which can be used in subsequent REST calls.
    The request data are:

    * client_id: the id of an OAuth2 client as configured in database
    * client_secret: the client secret,
    * grant_type: password|pincode,
    * username: the username,
    * password|pincode: the password or the pincode depending on the grant_type value,
    * taskgroup: the id of the taskgroup of the user

    :reqheader Content-Type: application/json
    :resheader Content-Type: application/json

    **Example of correct response**

    .. sourcecode:: json

        {"access_token": "25735f2de89eff6fa7576b7f8ca5efb952a23ef7",
         "expires_in": 31535999,
         "refresh_token": "e2a310b568aba5f92bf8683715f862b98b1d714d",
         "scope": "read",
         "token_type": "Bearer"
         }
