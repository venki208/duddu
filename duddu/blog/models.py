from __future__ import unicode_literals

from django.db import models

class Blog(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()

	def __str__(self):
		return self.name


class Author(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()

	def __str__(self):
		return self.name

class Entry(models.Model):
	blog = models.ForignKey(Blog)
	headline = models.CharField(max_length = 255)
