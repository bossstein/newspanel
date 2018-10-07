# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import datetime

# Create your models here.

# Creating the Auther class. This could be extended to include more author attributes.
class Author(models.Model):
	author_label = "Auther"
	author_name = models.CharField(max_length=64)
	def __str__(self):
		return self.author_name

# Creating the catagory class.
class Category(models.Model):
	category_label = "Catagory"
	category_name = models.CharField(max_length=64)
	def __str__(self):
		return self.category_name

# Creating the Publication Status class.
class Pub_status(models.Model):
	pub_status_label = "Publication Status"
	pub_status_name = models.CharField(max_length=64)
	def __str__(self):
		return self.pub_status_name

# Creating the Article class.
class Article(models.Model):
	# Title of article
	title_label = "Title"
	title = models.CharField(max_length=64)
	# Summary of article
	summary_label = "Summary"
	summary = models.CharField(max_length=256)
	# Text of article	
	content_label = "Content"
	content = models.TextField()
	# Auther of article. This could be extended to include multiple authors.
	author = models.ForeignKey( Author, on_delete=models.CASCADE)
	# Catagory of article. This could be extended to include multiple categories with a priority to determine ordering.
	category = models.ForeignKey( Category , on_delete=models.CASCADE)
	# Published status of article. Further functionality required so that only recent pulished articles are be visible to casual user.
	pub_status = models.ForeignKey( Pub_status , on_delete=models.CASCADE)

	# Date of publication
	published_date_label = "Published Date"
	published_date = models.DateTimeField(blank=True, null=True)

	def published_date_string(self):
		return self.published_date.strftime('%Y-%m-%dT%H:%M')
	def __str__(self):
		return self.title
	def was_published_recently(self):
		return (self.published_date) >= (timezone.now() - datetime.timedelta(days=3))

	edit_label = "Edit"
