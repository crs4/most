#
# Project MOST - Moving Outcomes to Standard Telemedicine Practice
# http://most.crs4.it/
#
# Copyright 2014, CRS4 srl. (http://www.crs4.it/)
# Dual licensed under the MIT or GPL Version 2 licenses.
# See license-GPLv2.txt or license-MIT.txt
#
import logging

from most.web.users.models import MostUser

class ApplicantBackend(object):

    def authenticate(self, username=None, pincode=None):

        logging.error('try to filter %s %s ' % (username, pincode))

        try:
            logging.error('Try to retrieve user %s with pin %s' % (username, pincode))
            user = MostUser.objects.get(username=username, numeric_password=pincode)
            return user

        except MostUser.DoesNotExist:

            return None

    def get_user(self, user_id):
            try:
                return MostUser.objects.get(pk=user_id)
            except MostUser.DoesNotExist:
                return None