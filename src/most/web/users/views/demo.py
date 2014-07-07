# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, get_list_or_404, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.utils.translation import ugettext as _
import json
from datetime import date, datetime


def examples(request):
    response = render_to_response('demo.html')
    return response