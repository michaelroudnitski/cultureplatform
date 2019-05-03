from django.conf.urls import url, include
from . import views

urlpatterns = [
    url("users/", include('users.urls')),
    url("forum/", include('forum.urls')),
    url("learn", views.learn, name='learn'),
    url('', views.index, name='index'),
]