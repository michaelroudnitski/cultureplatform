from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('create/', views.create, name='create'),
    url('', views.forum, name='forum'),
]