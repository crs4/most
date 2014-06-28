from django.conf.urls import patterns, include, url
from users.views import clinician_user, task_group, most_user, demo
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'most.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^demo/', demo.examples),
    url(r'^admin/', include(admin.site.urls)),
)

# MostUser API related urls
urlpatterns += patterns('',
    (r'^user/new/$', most_user.new),
    (r'^user/login/$', most_user.login_view),
    (r'^user/logout/$', most_user.logout_view),
    (r'^user/(?P<user_id>\d+)/get_user_info/$', most_user.get_user_info),
    (r'^user/filter/$', most_user.full_text_filter),
    (r'^user/(?P<user_id>\d+)/edit/$', most_user.edit),
    (r'^user/(?P<user_id>\d+)/deactivate/$', most_user.deactivate),
    (r'^user/(?P<user_id>\d+)/activate/$', most_user.activate),
)

# ClinicianUser API related urls
urlpatterns += patterns('',
    (r'^clinician/(?P<clinician_id>\d+)/is_provider/$', clinician_user.is_provider),  # get
    (r'^clinician/(?P<clinician_id>\d+)/set_provider/$', clinician_user.set_provider),  # post -> true | false
)


# TaskGroup API related urls
urlpatterns += patterns('',
    (r'^task_group/(?P<task_group_id>\d+)/is_provider/$', task_group.is_provider),  # get
    (r'^task_group/(?P<task_group_id>\d+)/set_provider/$', task_group.set_provider),  # post -> true | false
    (r'^task_group/(?P<task_group_id>\d+)/add_user/(?P<user_id>\d+)/$', task_group.add_user),
    (r'^task_group/(?P<task_group_id>\d+)/remove_user/(?P<user_id>\d+)/$', task_group.remove_user),
    (r'^task_group/(?P<task_group_id>\d+)/list_users/$', task_group.list_users),
    (r'^task_group/(?P<task_group_id>\d+)/add_related_task_group/(?P<related_task_group_id>\d+)/$',
     task_group.add_related_task_group),
    (r'^task_group/(?P<task_group_id>\d+)/remove_related_task_group/(?P<related_task_group_id>\d+)/$',
     task_group.remove_related_task_group),
    (r'^task_group/(?P<task_group_id>\d+)/list_related_task_groups/$', task_group.list_related_task_groups),
    (r'^task_group/(?P<task_group_id>\d+)/has_clinicians/$', task_group.has_clinicians),
    (r'^task_group/(?P<task_group_id>\d+)/list_clinicians/$', task_group.list_clinicians),
    (r'^task_group/(?P<task_group_id>\d+)/has_clinician_provider/$', task_group.has_clinician_provider),
    (r'^task_group/(?P<task_group_id>\d+)/list_clinician_providers/$', task_group.list_clinician_providers),
)