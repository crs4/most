# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.utils.translation import ugettext as _
import json
from datetime import date, datetime
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from . import staff_check
from . import DATA_KEY, ERRORS_KEY, MESSAGE_KEY, SUCCESS_KEY, TOTAL_KEY
from ..models import MostUser


@csrf_exempt
@login_required
@user_passes_test(staff_check)
def new(request):
    pass


@csrf_exempt
def login_view(request):
    result = {}
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    result[SUCCESS_KEY] = True
                    result[MESSAGE_KEY] = _('Welcome %s.' % user.username)
                    result[DATA_KEY] = user.to_dictionary()
                else:
                    result[ERRORS_KEY] = _('User %s disabled.' % user.pk)
                    result[SUCCESS_KEY] = False
                    # TODO: add (error_code, error_description) couple in DATA_KEY
            else:
                result[ERRORS_KEY] = _('Invalid login.')
                result[SUCCESS_KEY] = False
                # TODO: add (error_code, error_description) couple in DATA_KEY
        except Exception, e:
            result[ERRORS_KEY] = e
            result[SUCCESS_KEY] = False
    else:
        result[ERRORS_KEY] = _('POST method required.\n')
        result[SUCCESS_KEY] = False
    return HttpResponse(json.dumps(result), content_type='application/json; charset=utf8')


def logout_view(request):
    logout(request)
    result = {
        SUCCESS_KEY: True,
        MESSAGE_KEY: 'Bye.'
    }
    return HttpResponse(json.dumps(result), content_type='application/json; charset=utf8')


@login_required
def get_user_info(request, user_id):
    results = {}
    try:
        user = MostUser.objects.get(pk=user_id)
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('User %s found.' % user_id)
        results[DATA_KEY] = user.to_dictionary()
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


@require_GET
@login_required
def search(request):
    result = {}
    query_set = (Q())
    try:
        query_string = request.GET['query_string']
        query_list = [query for query in query_string.split(' ') if query]
        for query in query_list:
            query_set = query_set & (
                Q(username__icontains=query) |
                Q(last_name__icontains=query) |
                Q(first_name__icontains=query) |
                Q(email__icontains=query) |
                Q(certified_email__icontains=query)
            )
        users = MostUser.objects.filter(query_set)
        count_users = users.count()
        result[DATA_KEY] = []
        if count_users:
            for user in users:
                result[DATA_KEY].append(user.to_dictionary())
            result[MESSAGE_KEY] = _('%(users_count)s users found for query string: \'%(query_string)s\'' %
                                    {'users_count': count_users, 'query_string': query_string})
        else:
            result[MESSAGE_KEY] = _('No users found for query string: \'%s\'' % query_string)
        result[SUCCESS_KEY] = True
        result[TOTAL_KEY] = count_users
    except Exception, e:
        result[ERRORS_KEY] = e
        result[SUCCESS_KEY] = False
    return HttpResponse(json.dumps(result), content_type='application/json; charset=utf8')


@require_POST
@login_required
def edit(request):
    pass


@login_required
@user_passes_test(staff_check)
def deactivate(request, user_id):
    # solo chi e' staff, su user del proprio task group
    results = {}
    try:
        user = MostUser.objects.get(pk=user_id)
        user.is_active = False
        user.save()
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('User %s deactivated' % user_id)
        results[DATA_KEY] = {'id': user_id, 'is_active': user.is_active}
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')

@login_required
@user_passes_test(staff_check)
def activate(request, user_id):
    # solo chi e' staff, su user del proprio task group
    results = {}
    try:
        user = MostUser.objects.get(pk=user_id)
        user.is_active = True
        user.save()
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('User %s deactivated' % user_id)
        results[DATA_KEY] = {'id': user_id, 'is_active': user.is_active}
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


