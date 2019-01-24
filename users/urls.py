from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^r/$', views.register),
    url(r'^l/$', views.login),
    url(r'^addUser/$', views.add_user)

]