from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    url('', views.index, name='index'),
    path("users", include('users.urls')),
]