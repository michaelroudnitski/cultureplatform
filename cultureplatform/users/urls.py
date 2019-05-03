from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url('signup', views.signup, name='signup'),
    url('signin', views.signin, name='signin'),
    url('edit-profile', views.edit_profile, name='edit_profile'),
    url('signout', views.signout, name='signout'),
    url('password-change', auth_views.PasswordChangeView.as_view(), name='password_change'),
    url('password-change/done', auth_views.PasswordResetCompleteView .as_view(), name='password_change_done'),
]
