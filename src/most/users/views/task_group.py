# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.utils.translation import ugettext as _
import json
from datetime import date, datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test
from . import staff_check, SUCCESS_KEY, MESSAGE_KEY, TOTAL_KEY, ERRORS_KEY, DATA_KEY
from ..models import TaskGroup, MostUser


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
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(hospital__icontains=query)
            )
        task_groups = TaskGroup.objects.filter(query_set)
        count_task_groups = task_groups.count()
        result[DATA_KEY] = []
        if count_task_groups:
            for task_group in task_groups:
                result[DATA_KEY].append(task_group.to_dictionary(exclude_users=True, exclude_related_task_groups=True))
            result[MESSAGE_KEY] = _('%(count_task_groups)s task groups found for query string: \'%(query_string)s\'' %
                                    {'count_task_groups': count_task_groups, 'query_string': query_string})
        else:
            result[MESSAGE_KEY] = _('No task groups found for query string: \'%s\'' % query_string)
        result[SUCCESS_KEY] = True
        result[TOTAL_KEY] = count_task_groups
    except Exception, e:
        result[ERRORS_KEY] = e
        result[SUCCESS_KEY] = False
    return HttpResponse(json.dumps(result), content_type='application/json; charset=utf8')


@csrf_exempt
@login_required
# @user_passes_test add test for admin
def new(request):
    pass


@csrf_exempt
@login_required
# @user_passes_test add test for admin OR staff + same task group
def edit(request, task_group_id):
    pass


def list_available_states(request):
    results = {}
    try:
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('Task group API available activation states found.')
        results[DATA_KEY] = TaskGroup.ACTIVATION_STATES
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


@csrf_exempt
@login_required
@require_POST
# @user_passes_test add test for admin
def set_active_state(request, task_group_id, active_state):
    results = {}
    try:
        task_group = TaskGroup.objects.get(pk=task_group_id)
        task_group.is_active = TaskGroup.ACTIVATION_STATES[active_state]
        task_group.save()
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('Task group %s has %s activation state' % (task_group_id, active_state))
        results[DATA_KEY] = {'id': task_group_id, 'is_active': task_group.is_active}
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


@login_required
def is_provider(request, task_group_id):
    results = {}
    try:
        task_group = TaskGroup.objects.get(pk=task_group_id)
        results[SUCCESS_KEY] = True
        if task_group.is_health_care_provider:
            results[MESSAGE_KEY] = _('Task group %s is health care provider' % task_group_id)
        else:
            results[MESSAGE_KEY] = _('Task group %s not health care provider' % task_group_id)
        results[DATA_KEY] = {'id': task_group_id, 'is_health_care_provider': task_group.is_health_care_provider}
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


@csrf_exempt
@login_required
def set_provider(request, task_group_id):
    results = {}
    try:
        task_group = TaskGroup.objects.get(pk=task_group_id)
        task_group.is_health_care_provider = True
        task_group.save()
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('Task group %s is now health care provider' % task_group_id)
        results[DATA_KEY] = {'id': task_group_id, 'is_health_care_provider': task_group.is_health_care_provider}
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


@csrf_exempt
@login_required
# @user_passes_test add test for admin OR staff + same task group
def add_user(request, task_group_id, user_id):
    results = {}
    try:
        task_group = TaskGroup.objects.get(pk=task_group_id)
        user = MostUser.objects.get(pk=user_id)
        if not user.task_group_related.filter(pk=task_group_id):
            task_group.users.add(user)
            task_group.save()
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('User %s in task group %s' % (user_id, task_group_id))
        results[DATA_KEY] = {'task_group_id': task_group_id, 'user_id': user_id}
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


@csrf_exempt
@login_required
# @user_passes_test add test for admin OR staff + same task group
def remove_user(request, task_group_id, user_id):
    results = {}
    try:
        task_group = TaskGroup.objects.get(pk=task_group_id)
        user = MostUser.objects.get(pk=user_id)
        if user.task_group_related.filter(pk=task_group_id):
            task_group.users.remove(user)
            task_group.save()
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('User %s no more in task group %s' % (user_id, task_group_id))
        results[DATA_KEY] = {'task_group_id': task_group_id, 'user_id': user_id}
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


@login_required
def list_users(request, task_group_id):
    results = {}
    try:
        users = TaskGroup.objects.get(pk=task_group_id).users.all()
        users_list = []
        for user in users:
            users_list.append(user.to_dictionary())
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('Users of task group %s found.' % task_group_id)
        results[DATA_KEY] = users_list
        results[TOTAL_KEY] = users.count()
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


@csrf_exempt
@login_required
# @user_passes_test add test for admin OR staff + same task group
def add_related_task_group(request, task_group_id, related_task_group_id):
    results = {}
    try:
        task_group = TaskGroup.objects.get(pk=task_group_id)
        related_task_group = TaskGroup.objects.get(pk=related_task_group_id)
        if not related_task_group.specialist_task_group.filter(pk=task_group_id):
            task_group.related_task_groups.add(related_task_group)
            task_group.save()
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('Task group %s related to task groups of %s' % (related_task_group, task_group_id))
        results[DATA_KEY] = {'task_group_id': task_group_id, 'related_task_group_id': related_task_group_id}
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


@csrf_exempt
@login_required
# @user_passes_test add test for admin OR staff + same task group
def remove_related_task_group(request, task_group_id, related_task_group_id):
    results = {}
    try:
        task_group = TaskGroup.objects.get(pk=task_group_id)
        related_task_group = TaskGroup.objects.get(pk=related_task_group_id)
        if related_task_group.specialist_task_group.filter(pk=task_group_id):
            task_group.related_task_groups.remove(related_task_group)
            task_group.save()
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('Task group %s no more in related task groups of %s' % (related_task_group_id,
                                                                                         task_group_id))
        results[DATA_KEY] = {'task_group_id': task_group_id, 'related_task_group_id': related_task_group_id}
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


@login_required
def list_related_task_groups(request, task_group_id):
    results = {}
    try:
        related_task_groups = TaskGroup.objects.get(pk=task_group_id).related_task_groups.all()
        related_task_groups_list = []
        for related_task_group in related_task_groups:
            related_task_groups_list.append(related_task_group.to_dictionary(exclude_users=True,
                                                                             exclude_related_task_groups=True))
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('Related task groups of task group %s found.' % task_group_id)
        results[DATA_KEY] = related_task_groups_list
        results[TOTAL_KEY] = related_task_groups.count()
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


@login_required
def has_clinicians(request, task_group_id):
    results = {}
    try:
        task_group = TaskGroup.objects.get(pk=task_group_id)
        clinicians_count = task_group.clinicians_count()
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('Task group %s has %s clinician users.' % (task_group_id, clinicians_count))
        results[DATA_KEY] = {'task_group_id': task_group_id, 'clinicians_count': clinicians_count}
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


@login_required
def list_clinicians(request, task_group_id):
    results = {}
    try:
        clinician_users = TaskGroup.objects.get(pk=task_group_id).users.filter(clinician_related__isnull=False)
        clinician_users_list = []
        for clinician_user in clinician_users:
            clinician_users_list.append(clinician_user.to_dictionary())
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('Clinician users of task group %s found.' % task_group_id)
        results[DATA_KEY] = clinician_users_list
        results[TOTAL_KEY] = clinician_users.count()
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


@login_required
def has_clinician_provider(request, task_group_id):
    results = {}
    try:
        clinician_provider_users = TaskGroup.objects.get(pk=task_group_id).users.filter(
            clinician_related__isnull=False, clinician_related__is_health_care_provider=True)
        clinician_providers_count = clinician_provider_users.count()
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('Task group %s has %s clinician provider users.' %
                                 (task_group_id, clinician_providers_count))
        results[DATA_KEY] = {'task_group_id': task_group_id, 'clinicians_count': clinician_providers_count}
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')


@login_required
def list_clinician_providers(request, task_group_id):
    results = {}
    try:
        clinician_provider_users = TaskGroup.objects.get(pk=task_group_id).users.filter(
            clinician_related__isnull=False, clinician_related__is_health_care_provider=True)
        clinician_provider_users_list = []
        for clinician_provider_user in clinician_provider_users:
            clinician_provider_users_list.append(clinician_provider_user.to_dictionary())
        results[SUCCESS_KEY] = True
        results[MESSAGE_KEY] = _('Clinician provider users of task group %s found.' % task_group_id)
        results[DATA_KEY] = clinician_provider_users_list
        results[TOTAL_KEY] = clinician_provider_users.count()
    except Exception, e:
        results[SUCCESS_KEY] = False
        results[ERRORS_KEY] = e
    return HttpResponse(json.dumps(results), content_type='application/json; charset=utf8')
