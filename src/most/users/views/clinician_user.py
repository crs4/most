# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.utils.translation import ugettext as _
import json
from datetime import date, datetime
from django.db.models import Q
from . import staff_check
from ..models import ClinicianUser
from django.contrib.auth.decorators import login_required, user_passes_test
from . import staff_check, SUCCESS_KEY, MESSAGE_KEY, TOTAL_KEY, ERRORS_KEY, DATA_KEY


@login_required
def is_provider(request, user_id):
    results = {}
    try:
        clinician_user = ClinicianUser.objects.get(user__pk=user_id)
        results[SUCCESS_KEY] = True
        if clinician_user.is_health_care_provider:
            results[MESSAGE_KEY] = _('User %s is health care provider' % user_id)
        else:
            results[MESSAGE_KEY] = _('User %s not health care provider' % user_id)
        results[DATA_KEY] = {'user_id': user_id, 'is_health_care_provider': clinician_user.is_health_care_provider}
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


@csrf_exempt
@login_required
def set_provider(request, user_id):
    results = {}
    try:
        clinician_user = ClinicianUser.objects.get(user__pk=user_id)
        clinician_user.is_health_care_provider = True
        clinician_user.save()
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('User %s is now health care provider' % user_id)
        results[DATA_KEY] = {'user_id': user_id, 'is_health_care_provider': clinician_user.is_health_care_provider}
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
                Q(user__username__icontains=query) |
                Q(user__last_name__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__email__icontains=query) |
                Q(user__certified_email__icontains=query) |
                Q(specialization__icontains=query)
            )
        clinician_users = ClinicianUser.objects.filter(query_set)
        count_clinician_users = clinician_users.count()
        result[DATA_KEY] = []
        if count_clinician_users:
            for clinician_user in clinician_users:
                result[DATA_KEY].append(clinician_user.to_dictionary())
            result[MESSAGE_KEY] = _('%(clinician_users_count)s users found for query string: \'%(query_string)s\'' %
                                    {'clinician_users_count': count_clinician_users, 'query_string': query_string})
        else:
            result[MESSAGE_KEY] = _('No clinician users found for query string: \'%s\'' % query_string)
        result[SUCCESS_KEY] = True
        result[TOTAL_KEY] = count_clinician_users
    except Exception, e:
        result[ERRORS_KEY] = e
        result[SUCCESS_KEY] = False
    return HttpResponse(json.dumps(result), content_type='application/json; charset=utf8')


@login_required
def get_user_info(request, user_id):
    results = {}
    try:
        clinician_user = ClinicianUser.objects.get(user__pk=user_id)
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('Clinician user %s found.' % user_id)
        results[DATA_KEY] = clinician_user.user.to_dictionary()
        print results[DATA_KEY]
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')