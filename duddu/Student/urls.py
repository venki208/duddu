from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^(?P<question_id>[0-9]+)/$', views.detailed_information, name="information"),
	url(r'^(?P<question_id>[0-9]+)/result/$', views.student_result, name="student_result"),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]