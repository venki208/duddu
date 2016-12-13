from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE, null=True)
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return '%s' %(self.question_text)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)

	def __str__(self):
		return '%s' %(self.choice_text)
