from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'', views.all_news, name='all_news')
]