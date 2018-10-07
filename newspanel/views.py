# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from datetime import datetime
from .util import create_default_authors
from .util import create_default_categories
from .util import create_default_pub_status

from .models import Article
from .models import Category
from .models import Author
from .models import Pub_status
from .util import xml_feed

# Create your views here.

# List of articles
def index(request):
    create_default_authors()
    create_default_categories()
    create_default_pub_status()
    # Populating list of articles
    latest_article_list = Article.objects.order_by('-published_date')
    context = {'latest_article_list' : latest_article_list}
    return HttpResponse(render(request,'newspanel/index.html',context))

# Simple article reading view.
def detail(request, article_id):
    # Retrieve article
    article = get_object_or_404( Article , pk=article_id )
    return render(request, 'newspanel/detail.html', {'article': article})

# Returns an XML file to populate an APP.
def app_req(request):
    return HttpResponse(xml_feed(),content_type='application/xml')

# An editable article view.
def edit_article(request, article_id):

    # Populate lists of objects available for selection when editing the article
    category_list = Category.objects.order_by('-category_name')
    author_list = Author.objects.order_by('-author_name')
    pub_status_list = Pub_status.objects.order_by('-pub_status_name')

    # Retrieve article
    article = get_object_or_404(Article, pk=article_id)
    context = { 'category_list': category_list ,
                'author_list' : author_list ,
                'pub_status_list': pub_status_list,
                'article' : article,}
    return render(request, 'newspanel/edit_article.html', context)

# Action on 'Submit Edit' button on edit_article view.
def submit_edit(request, article_id):

    # Retrieve article
    article = get_object_or_404(Article, pk=article_id)

    # Edit values and save changes.
    article.title           = request.POST['title']
    article.author          = Author(int(request.POST['author']))
    article.category        = Category(int(request.POST['category']))
    article.pub_status      = Pub_status(int(request.POST['pub_status']))
    article.published_date  = datetime.strptime(request.POST['published_date'],'%Y-%m-%dT%H:%M')
    article.summary         = request.POST['summary']
    article.content         = request.POST['content']
    article.save()

    # Redirect to detail view to see the results.
    return HttpResponseRedirect(reverse('newspanel:detail', args=(article.id,)))

# New article creation.
def new_article(request):

    # Populate lists of objects available for selection when editing the article
    category_list = Category.objects.order_by('-category_name')
    author_list = Author.objects.order_by('-author_name')
    pub_status_list = Pub_status.objects.order_by('-pub_status_name')

    # Create Article with default values
    article = Article.objects.create(
        title = Article.title_label,
        summary = Article.summary_label,
        author = author_list[0],
        category = category_list[0],
        pub_status = pub_status_list[0],
        published_date = datetime.now(),
        content = Article.content_label
    )

    context = { 'category_list': category_list ,
                'author_list' : author_list ,
                'pub_status_list': pub_status_list,
                'article' : article,}


    return render(request, 'newspanel/edit_article.html', context)



