# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import datetime

# Create your models here.

# Creating the auther class
class Author(models.Model):
	author_label = "Auther"
	author_name = models.CharField(max_length=64)
	def __str__(self):
		return self.author_name

# Creating the catagory class
class Catagory(models.Model):
	catagory_label = "Catagory"
	catagory_name = models.CharField(max_length=64)
	def __str__(self):
		return self.catagory_name

# Creating the Publication Status class
class Pub_status(models.Model):
	pub_status_label = "Publication Status"
	pub_status_name = models.CharField(max_length=64)
	def __str__(self):
		return self.pub_status_name

# Creating the article class
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
	# Auther of article
	author = models.ForeignKey( Author, on_delete=models.CASCADE)
	# Catagory of article
	catagory = models.ForeignKey( Catagory , on_delete=models.CASCADE)
	# Published status of article wherin only pulished should be visible to end user
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
