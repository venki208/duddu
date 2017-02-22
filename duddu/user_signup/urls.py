from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.index, name='signup'),
	url(r'^home/$', TemplateView.as_view(template_name="home.html")),
]