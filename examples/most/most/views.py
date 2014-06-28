# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, get_list_or_404, render_to_response
from django.http import Http404
from django.core.context_processors import csrf
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.utils.translation import get_language


def examples(request):
    context = RequestContext(request)
    context.update(csrf(request))
    response = render_to_response('users/demo.html', context)
    response.set_cookie("django_language", get_language())
    return response