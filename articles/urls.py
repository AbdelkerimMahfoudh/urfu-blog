
from django.urls import path
from . import views
app_name='articles'
urlpatterns = [
    path('',views.articles,name='list'),
    path('<str:slug>/',views.articles_details,name='detail'),
    path('create_art',views.create_article,name='create_article')
]
