from django.shortcuts import render
import datetime, json
from provider.oauth2.models import AccessToken
from most.web.authentication.decorators import oauth2_required
from django.http import HttpResponse
import pytz

@oauth2_required
def test_auth(request):

	return HttpResponse(json.dumps({'success' : True, 'data' : {'username' : request.user.username}}), content_type="application/json")


