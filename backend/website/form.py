from django import forms
from django.forms import ModelForm
from .models import Dog, Service, Galery

class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = "__all__"

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"

class GalleryForm(ModelForm):
    class Meta:
        model = Galery
        fields = "__all__"

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=30)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

