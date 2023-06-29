from django import forms
from django.forms import ModelForm
from .models import Dog, Service

class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = "__all__"

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"

