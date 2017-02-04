from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
	return render(request, 'login/login.html', locals())

def user_login(request):
	username = request.POST['email']
	password = request.POST['password']
	user = authenticate(username = username, password = password)
	if user:
		login(request, user)
	return redirect('/')