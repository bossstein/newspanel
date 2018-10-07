from django.urls import path

from . import views

app_name = 'newspanel'

# Url patterns for  reference in views and html.
urlpatterns = [
    path('', views.index, name='index'),
	path('<int:article_id>/', views.detail, name='detail'),
	path('app_req/', views.app_req, name='app_req'),
    path('<int:article_id>/edit_article/', views.edit_article, name='edit_article'),
    path('<int:article_id>/submit_edit/', views.submit_edit, name='submit_edit'),
    path('new_article/', views.new_article, name='new_article'),
]
