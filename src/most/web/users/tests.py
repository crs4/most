#
# Project MOST - Moving Outcomes to Standard Telemedicine Practice
# http://most.crs4.it/
#
# Copyright 2014, CRS4 srl. (http://www.crs4.it/)
# Dual licensed under the MIT or GPL Version 2 licenses.
# See license-GPLv2.txt or license-MIT.txt

from django.test import TestCase
from django.core.urlresolvers import reverse
from most.web.users.models import User, ClinicianUser, TaskGroup
import json
from django.db.models import Q


class TaskGroupAPITest(TestCase):
    """
    /users/task_group/search/
    /users/task_group/new/
    /users/task_group/(?P<task_group_id>\d+)/get_task_group_info/
    /users/task_group/(?P<task_group_id>\d+)/edit/
    /users/task_group/list_available_states/
    /users/task_group/(?P<task_group_id>\d+)/set_active_state/(?P<active_state>\w+)/
    /users/task_group/(?P<task_group_id>\d+)/is_provider/
    /users/task_group/(?P<task_group_id>\d+)/set_provider/
    /users/task_group/(?P<task_group_id>\d+)/add_user/(?P<user_id>\d+)/
    /users/task_group/(?P<task_group_id>\d+)/remove_user/(?P<user_id>\d+)/
    /users/task_group/(?P<task_group_id>\d+)/list_users/
    /users/task_group/(?P<task_group_id>\d+)/add_related_task_group/(?P<related_task_group_id>\d+)/
    /users/task_group/(?P<task_group_id>\d+)/remove_related_task_group/(?P<related_task_group_id>\d+)/
    /users/task_group/(?P<task_group_id>\d+)/list_related_task_groups/
    /users/task_group/(?P<task_group_id>\d+)/has_clinicians/
    /users/task_group/(?P<task_group_id>\d+)/list_clinicians/
    /users/task_group/(?P<task_group_id>\d+)/has_clinician_provider/
    /users/task_group/(?P<task_group_id>\d+)/list_clinician_providers/
    """
    pass


class UserAPITest(TestCase):
    """
    /users/user/new/
    /users/user/(?P<user_id>\d+)/get_user_info/
    /users/user/search/
    /users/user/(?P<user_id>\d+)/edit/
    /users/user/(?P<user_id>\d+)/deactivate/
    /users/user/(?P<user_id>\d+)/activate/
    /users/user/logout/
    """
    pass


class ClinicianUserAPITest(TestCase):
    """
    /users/clinician_user/(?P<user_id>\d+)/is_provider/
    /users/clinician_user/(?P<user_id>\d+)/set_provider/
    /users/clinician_user/search/
    /users/clinician_user/(?P<user_id>\d+)/get_user_info/
    """
    pass