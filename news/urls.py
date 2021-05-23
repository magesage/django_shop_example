from django.urls import path
from .views import *

urlpatterns = [
    path('', news_list, name='news_list_url'),
    path('article/<str:slug>/', news_article, name='news_article_url'),
]