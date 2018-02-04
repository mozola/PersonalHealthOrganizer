from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^all_news/', views.all_news, name='all_news')
]