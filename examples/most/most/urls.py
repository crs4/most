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

    # Task Group
    url(r'^task_group/is_provider', 'most.views.task_group_is_provider'),
    url(r'^task_group/set_provider', 'most.views.task_group_set_provider'),
    url(r'^task_group/set_active_state', 'most.views.task_group_set_active_state'),
    url(r'^task_group/add_user', 'most.views.task_group_add_user'),
    url(r'^task_group/remove_user', 'most.views.task_group_remove_user'),
    url(r'^task_group/list_users', 'most.views.task_group_list_users'),
    url(r'^task_group/add_related_task_group', 'most.views.task_group_add_related_task_group'),
    url(r'^task_group/remove_related_task_group', 'most.views.task_group_remove_related_task_group'),
    url(r'^task_group/list_related_task_group', 'most.views.task_group_list_related_task_group'),
    url(r'^task_group/has_clinicians', 'most.views.task_group_has_clinicians'),
    url(r'^task_group/list_clinicians', 'most.views.task_group_list_clinicians'),
    url(r'^task_group/has_clinician_provider', 'most.views.task_group_has_clinician_provider'),
    url(r'^task_group/list_clinician_providers', 'most.views.task_group_list_clinician_providers'),
    url(r'^task_group/search', 'most.views.task_group_search'),

    # Most User
    url(r'^most_user/get_user_info/', 'most.views.most_user_get_user_info'),
    url(r'^most_user/search/', 'most.views.most_user_search'),
    url(r'^most_user/deactivate/', 'most.views.most_user_deactivate'),
    url(r'^most_user/activate/', 'most.views.most_user_activate'),

    # Clinician User
    url(r'^clinician_user/search/', 'most.views.clinician_user_search'),
    url(r'^clinician_user/get_user_info/', 'most.views.clinician_user_get_user_info'),
    url(r'^clinician_user/is_provider/', 'most.views.clinician_user_is_provider'),
    url(r'^clinician_user/set_provider/', 'most.views.clinician_user_set_provider'),
)
