from django.db import models


class Article(models.Model):
	title = models.CharField(max_length=200, blank=True)
	author = models.CharField(max_length=200, blank=True)
	email = models.EmailField(max_length=200, blank=True)
	date = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.title