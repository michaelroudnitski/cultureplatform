from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('create/', views.create, name='create'),
    url('categories/culture_and_diversity', views.cultural_and_diversity, name='cul_and_diversity'),
    url('12345', views.liveforum, name='liveforum'),
    url('categories/philosophy_and_ethics', views.philosophy_and_ethics, name='philosophy_and_ethics'),
    url('categories/mental_health', views.mental_health, name='mental_health'),
    url('categories/miscellaneous', views.miscellaneous, name='miscellaneous'),
    url('', views.forum, name='forum'),

]