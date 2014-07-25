#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

USERNAME = 'valeria'
PASSWORD = 'valleria'

HOST_ADDRESS = 'http://127.0.0.1:8000'

s = requests.session()
s.post('%s/users/user/login/' % HOST_ADDRESS, data={'username': USERNAME, 'password': PASSWORD})


def print_response_data(class_name, dictionary):
    print u'JSON response: %s\n' % dictionary
    if dictionary['success']:
        # dump dictionary to print human readable data
        print u'%s data:\n%s' % (class_name, json.dumps(dictionary['data'], sort_keys=True, indent=4,
                                                        separators=(',', ': ')))
    else:
        print dictionary['errors']


def compose_post_request(api, data):
    print 'Calling %s\n' % api
    response = s.post('%s%s' % (HOST_ADDRESS, api), data=data)
    # print response.text
    return response.json()


def compose_get_request(api, params):
    print 'Calling %s\n' % api
    response = s.get('%s%s' % (HOST_ADDRESS, api), params={'query_string': params})
    return response.json()