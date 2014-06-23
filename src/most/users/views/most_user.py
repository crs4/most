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
    pass


@login_required
def full_text_filter(request):
    pass


@login_required
def edit(request):
    pass


@login_required
@user_passes_test(staff_check)
def deactivate(request, user_id):
    # solo chi e' staff, su user del proprio task group
    pass


@login_required
@user_passes_test(staff_check)
def activate(request, user_id):
    # solo chi e' staff, su user del proprio task group
    pass


