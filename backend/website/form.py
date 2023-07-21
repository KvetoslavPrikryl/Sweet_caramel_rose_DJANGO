from django import forms
from django.forms import ModelForm
from .models import User, Service, Galery, Link, Dog

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"

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
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

class LinkForm(forms.Form):
    class Meta:
        model = Link
        fields = "__all__"
