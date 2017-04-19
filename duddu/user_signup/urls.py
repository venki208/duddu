from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from .views import DemoForm, SignupForm, ListingEmails
urlpatterns = [
	url(r'^$', views.index, name='signup'),
	url(r'^home/$', TemplateView.as_view(template_name="home.html")),
	url(r'^demo_form/', DemoForm.as_view()),
	url(r'^user_signup/', SignupForm.as_view(), name="user_signup"),
	url(r'^list_email/', ListingEmails.as_view(), name="list_emails"),
]