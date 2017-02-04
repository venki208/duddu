from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="login" ),
	url(r'^user_login/', views.user_login, name='user_login'),
]