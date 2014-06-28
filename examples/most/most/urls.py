from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'most.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^users/', include('users.urls', namespace='users')), #urls of users app api
    url(r'^admin/', include(admin.site.urls)),
    url(r'^demo/', 'most.views.examples', name='examples'),
    url(r'^task_group/is_provider', 'most.views.task_group_is_provider'),
)
