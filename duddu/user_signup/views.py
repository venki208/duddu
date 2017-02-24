from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from Student.models import Question
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

# Create your views here.
@login_required()
def index(request):
	return render(request, 'index.html', locals())

class SignupForm(TemplateView):
	template_name = "user_signup/signup.html"