from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
	question = Question.objects.order_by('-pub_date')
	result = ', '.join([list_q.question_text for list_q in question])
	template = loader.get_template('Student/index.html')
	return HttpResponse(template.render(locals(), request))
	# we can send data to html by this way also
	# return render(request, 'Student/index.html', locals())

def detailed_information(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'Student/index.html', locals())

def student_result(request, question_id):
	response = 'Your result will comming soon for %s'
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse('Thank you for giving vote to %s question' % question_id)