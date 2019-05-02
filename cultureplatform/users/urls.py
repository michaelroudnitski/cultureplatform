from django.conf.urls import url

from . import views

urlpatterns = [
    url('login', views.login, name='login'),
    url('signup', views.signup, name='signup'),
]
