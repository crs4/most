from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^test$', "oauth.views.test_auth"),
)
