from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from .views import SignupForm
urlpatterns = [
	url(r'^$', views.index, name='signup'),
	url(r'^home/$', TemplateView.as_view(template_name="home.html")),
	url(r'^user_signup/', SignupForm.as_view()),
]