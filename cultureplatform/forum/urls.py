from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('create/', views.create, name='create'),
    url('/', views.forum, name='forum'),
    url('categories/culture_and_diversity/<int:id>', views.cultural_and_diversity, name='cul_and_diversity'),
    url('categories/philosophy_and_ethics/<int:id>', views.philosophy_and_ethics, name='philosophy_and_ethics'),
    url('categories/mental_health/<int:id>', views.mental_health, name='mental_health'),
    url('categories/miscellaneous/<int:id>', views.miscellaneous, name='miscellaneous'),

]