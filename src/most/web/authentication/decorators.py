#
# Project MOST - Moving Outcomes to Standard Telemedicine Practice
# http://most.crs4.it/
#
# Copyright 2014, CRS4 srl. (http://www.crs4.it/)
# Dual licensed under the MIT or GPL Version 2 licenses.
# See license-GPLv2.txt or license-MIT.txt

import functools
import datetime, json
from django.http import HttpResponse
from provider.oauth2.models import AccessToken
import pytz
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from most.web.users.models import TaskGroup


NO_TOKEN_PROVIDED = 101
ACCESS_DENIED = 102
TOKEN_EXPIRED = 103

def oauth2_required(method):
    @functools.wraps(method)
    def wrapper(request, *args, **kwargs):

        key = request.META.get('HTTP_AUTHORIZATION')
        if not key:
            if 'access_token' in request.REQUEST:
                key = request.REQUEST['access_token']
        if not key:
            return HttpResponse(json.dumps({'success': False,
                                            'data': {'error': 'No Token Provided.', 'code': NO_TOKEN_PROVIDED}}),
                                content_type="application/json")

        try:
            token = AccessToken.objects.get(token=key)
            if not token:
                return HttpResponse(json.dumps({'success': False,
                                                'data': {'error': 'Access denied.', 'code': ACCESS_DENIED}}),
                                    content_type="application/json")
            if token.expires < datetime.datetime.now(pytz.UTC):
                return HttpResponse(json.dumps({'success': False,
                                                'data': {'error': 'Token has expired.', 'code': TOKEN_EXPIRED}}),
                                    content_type="application/json")
            user = token.user
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)

            request.accesstoken = token

            # After login, Retrieve task group and set in request
            taskgroup = token.taskgroup
            request.taskgroup = taskgroup

            return method(request, *args, **kwargs)
        except ObjectDoesNotExist, ex:
            return HttpResponse(json.dumps({'success': False,
                                            'data': {'error': 'Token does not exists.', 'code': ACCESS_DENIED}}),
                                content_type="application/json")

    return wrapper
