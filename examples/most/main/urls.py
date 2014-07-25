from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^users/', include('web.users.urls', namespace='users')), #urls of users app api
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^demo/', 'main.views.examples', name='examples'),
    url(r'^test$',  "web.authentication.views.test_auth"),

    # Task Group
    url(r'^task_group/new', 'main.views.task_group_new'),
    url(r'^task_group/is_provider', 'main.views.task_group_is_provider'),
    url(r'^task_group/set_provider', 'main.views.task_group_set_provider'),
    url(r'^task_group/set_active_state', 'main.views.task_group_set_active_state'),
    url(r'^task_group/add_user', 'main.views.task_group_add_user'),
    url(r'^task_group/remove_user', 'main.views.task_group_remove_user'),
    url(r'^task_group/list_users', 'main.views.task_group_list_users'),
    url(r'^task_group/add_related_task_group', 'main.views.task_group_add_related_task_group'),
    url(r'^task_group/remove_related_task_group', 'main.views.task_group_remove_related_task_group'),
    url(r'^task_group/list_related_task_group', 'main.views.task_group_list_related_task_group'),
    url(r'^task_group/has_clinicians', 'main.views.task_group_has_clinicians'),
    url(r'^task_group/list_clinicians', 'main.views.task_group_list_clinicians'),
    url(r'^task_group/has_clinician_provider', 'main.views.task_group_has_clinician_provider'),
    url(r'^task_group/list_clinician_providers', 'main.views.task_group_list_clinician_providers'),
    url(r'^task_group/search', 'main.views.task_group_search'),

    # Most User
    url(r'^most_user/new/', 'main.views.most_user_new'),
    url(r'^most_user/get_user_info/', 'main.views.most_user_get_user_info'),
    url(r'^most_user/search/', 'main.views.most_user_search'),
    url(r'^most_user/deactivate/', 'main.views.most_user_deactivate'),
    url(r'^most_user/activate/', 'main.views.most_user_activate'),

    # Clinician User
    url(r'^clinician_user/search/', 'main.views.clinician_user_search'),
    url(r'^clinician_user/new/', 'main.views.clinician_user_new'),
    url(r'^clinician_user/get_user_info/', 'main.views.clinician_user_get_user_info'),
    url(r'^clinician_user/is_provider/', 'main.views.clinician_user_is_provider'),
    url(r'^clinician_user/set_provider/', 'main.views.clinician_user_set_provider'),
)
