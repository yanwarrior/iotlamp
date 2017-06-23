from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
	url(r'^lamps/$', views.LampList.as_view(), name="lamp_list"),
	url(r'^lamps/(?P<pk>[0-9]+)/$', views.LampDetail.as_view(), name="lamp_detail"),
	url(r'^schedules/$', views.ScheduleList.as_view(), name="schedule_list"),
	url(r'^schedules/(?P<pk>[0-9]+)/$', views.ScheduleDetail.as_view(), name="schedule_detail"),
	url(r'^logs/$', views.LogList.as_view(), name="log_list"),
	url(r'^logs/(?P<pk>[0-9]+)/$', views.LogDetail.as_view(), name="log_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)