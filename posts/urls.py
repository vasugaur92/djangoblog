from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^create/$', views.post_create, name='create'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='detail'),
    url(r'^list/$', views.post_list, name='list'),
    url(r'^(?P<id>\d+)/update/$', views.post_update, name='update'),
    url(r'^delete/$', views.post_delete, name='delete'),

]