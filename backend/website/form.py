from django import forms
from django.forms import ModelForm
from .models import User, Service, Galery, Dog, Link

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = "__all__"
        labels = {
            "name" : "Jméno",
            "color" : "Barva",
            "weight" : "Váha",
            "height" : "Výška",
            "patel" : "Patel",
            "body" : "Text ke psovi",
            "dog_sex" : "Pohlaví psa",
            "image1": "Obrázek 1",
            "image2" : "Obrázek 2",
            "image3" : "Obrázek 3"
        }
class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"

class GalleryForm(ModelForm):
    class Meta:
        model = Galery
        fields = "__all__"

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'contact-input'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'contact-textarea'}))



class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = "__all__"