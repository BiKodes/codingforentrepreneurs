from django.contrib import admin

from django.urls import path

from .views import (
    article_list_view,
    article_create_view,
    article_list_view,
    article_detail_view,
    dynamic_lookup_view,
    article_delete_view,
    article_update_view,
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

app_name ='blog'
urlpatterns = [
    path('',article_list_view, name = 'article_list'),
    path('',ArticleListView.as_view(), name = 'article_list'), #<blog>/<modelname>_list.html
    path('create/',article_create_view, name = 'article_create'),
    path('create/',ArticleCreateView.as_view(), name = 'article_create'),
    path('<int:id>/',article_list_view, name = 'article_list'),
    path('<int:id>/',article_detail_view, name = 'article_detail'),
    path('<int:id>/',ArticleDetailView.as_view(), name = 'article_detail'),
    path('<int:id>/',dynamic_lookup_view, name = 'dynamic_lookup'),
    path('<int:id>/delete/',article_delete_view, name = 'article_delete'),
    path('<int:id>/delete/',ArticleDeleteView.as_view(), name = 'article_delete'),
    path('<int:id>/update/',article_update_view, name = 'article_update'),
    path('<int:id>/update/',ArticleUpdateView.as_view(), name = 'article_update'),

]
