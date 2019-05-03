from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # url('login', LoginView.as_view(template_name='login.html'), name="login"),
    url('login', views.login, name='login'),
    url('signup', views.signup, name='signup'),
]
