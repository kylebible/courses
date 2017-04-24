from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addcourse$', views.addcourse),
    url(r'^deletecourse/(?P<id>\d)+/yes$', views.deletecourse),
    url(r'^deletecourse/(?P<id>\d)+$', views.confirmdelete)
]
