from django.urls import path
from . import views

urlpatterns = [
    path('articles', views.articles_list, name='articles_list'),
    path('<slug>', views.article_detail, name='article_detail'),
    path('article_create/', views.article_create, name="article_create"),
    path('<slug>/edit', views.article_edit, name="article_edit"),
    path('<slug>/delete', views.article_delete, name="article_delete"),
    path('<slug>/like', views.article_like, name='article_like'),
    path('<slug>/dislike', views.article_dislike, name='article_dislike'),
    path('<slug>/comment/<pk>/delete', views.delete_comment, name='delete_comment'),
    path('<slug>/comment/<pk>/edit', views.edit_comment, name='edit_comment'),
]
