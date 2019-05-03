from django import forms
from django.forms import ModelForm
from .models import Forum

class NewForumForm(ModelForm):
    """ inherits the Forum model and casts as a form """
    class Meta:
        model = Forum
        fields = ['title',]