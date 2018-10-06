# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Author
from .models import Article
from .models import Catagory
from .models import Pub_status

# Register your models here.

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Catagory)
admin.site.register(Pub_status)
