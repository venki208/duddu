from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from Student.models import Question
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from django.views import View

# Create your views here.
@login_required()
def index(request):
	return render(request, 'index.html', locals())

class DemoForm(TemplateView):
	model = User
	template_name = "user_signup/signup.html"

	# This will call when Request is Header Request
	def head(self, *args, **kwargs):
		user = User.objects.all()
		context = {
			'user' : user
		}
		return context

class SignupForm(View):
	def get(self, request):
		return render(request, 'user_signup/signup.html', locals())

	def post(self, request):
		return HttpResponseRedirect('/list_email/')

class ListingEmails(ListView):
	template_name = 'user_signup/email_ids.html'

	def get(self, request):
		user = User.objects.filter(username = 'venkateshraja08@gmail.com')
		# user = self.user.first()
		print user[0]
		user = user[0]
		return user