# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Author
from .models import Article
from .models import Category
from .models import Pub_status

# Register your models here.
# Here models are registered so that they can be altered by the admin interface.

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Pub_status)
