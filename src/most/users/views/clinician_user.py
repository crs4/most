# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.utils.translation import ugettext as _
import json
from datetime import date, datetime
from django.db.models import Q
from . import staff_check


def is_provider(request, clinician_id):
    pass


def set_provider(request, clinician_id):
    pass