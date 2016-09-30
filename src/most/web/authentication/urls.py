#
# Project MOST - Moving Outcomes to Standard Telemedicine Practice
# http://most.crs4.it/
#
# Copyright 2014, CRS4 srl. (http://www.crs4.it/)
# Dual licensed under the MIT or GPL Version 2 licenses.
# See license-GPLv2.txt or license-MIT.txt
from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'test/$', 'most.web.authentication.views.test_auth'),
    # url(r'test$', 'authentication.views.test_auth'),
)
