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
def is_provider(request, clinician_id):
    results = {}
    try:
        clinician_user = ClinicianUser.objects.get(pk=clinician_id)
        results[SUCCESS_KEY] = True
        if clinician_user.is_health_care_provider:
            results[MESSAGE_KEY] = _('User %s is health care provider' % clinician_id)
        else:
            results[MESSAGE_KEY] = _('User %s not health care provider' % clinician_id)
        results[DATA_KEY] = {'id': clinician_id, 'is_health_care_provider': clinician_user.is_health_care_provider}
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


@csrf_exempt
@login_required
def set_provider(request, clinician_id):
    results = {}
    try:
        clinician_user = ClinicianUser.objects.get(pk=clinician_id)
        clinician_user.is_health_care_provider = True
        clinician_user.save()
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('User %s is now health care provider' % clinician_id)
        results[DATA_KEY] = {'id': clinician_id, 'is_health_care_provider': clinician_user.is_health_care_provider}
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')