from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.core.mail import send_mail
from django.contrib import messages
from .models import User, Dog, Service, Galery
from .form import DogForm, ServiceForm, GalleryForm, ContactForm
from django.http import HttpResponseRedirect

def home(request):
    user_list = User.objects.all()


    if request.method == "POST":
        
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Jsi přihlášen.")
            return redirect("home")
        else :
            messages.success(request, "Nesprávné jméno nebo heslo.")
            return redirect("home")
    else: 
        return render(request, "home.html", {"user_list" : user_list})

def logout_user(request):
    logout(request)
    messages.success(request, "Byl jsi odhlášen")
    return redirect("home")

def kennel(request):
    dogs = Dog.objects.all()
    form = DogForm
    submitted = False
    dog_man = []
    dog_women = []
    puppy = []
    some_dogs = []
    for dog in dogs:
        if dog.dog_sex == "pes":
            dog_man.append(dog)
        elif dog.dog_sex == "fena":
            dog_women.append(dog)
        elif dog.dog_sex == "štěně":
            puppy.append(dog)
        else:
            some_dogs.append(dog)
            print(f"Nepodařilo se přidat tyto psy: {some_dogs}")
    if request.method == "POST":
        formular = DogForm(request.POST, request.FILES)
        if formular.is_valid():
            formular.save()
            return HttpResponseRedirect("/chovatelska_stanice?submitted=True")
    else:
        formular = DogForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "kennel.html", {
        "dog_man" : dog_man,
        "dog_women" : dog_women,
        "puppy" : puppy,
        "form": form,
        "submitted": submitted 
    })

def service(request):
    services = Service.objects.all()
    form = ServiceForm
    galery = Galery.objects.all()
    submitted = False
    if request.method == "POST":
        formular = ServiceForm(request.POST)
        if formular.is_valid():
            formular.save()
            return HttpResponseRedirect("/sluzby?submitted=True")
    else:
        formular = ServiceForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "service.html", {
        "services": services,
        "form" : form,
        "galery" : galery,
    })

def dog(request, pk):
    dog = Dog.objects.get(pk=pk)
    form = DogForm(request.POST or None, instance=dog)
    if form.is_valid():
        form.save()
        return redirect("kennel")
    return render(request, "update.html", {
        "form": form
        })

def galery(request):
    form = GalleryForm
    galery = Galery.objects.all()
    services = Service.objects.all()
    submitted = False
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("gallery")
        else:
            form = GalleryForm
            if "submitted" in request.GET:
                submitted = True
    return render(request, "gallery.html", {
        "form" : form,
        "galery" : galery,
        "services" : services
    })


def delete_dog(request, pk):
    dog = Dog.objects.get(pk=pk)
    dog.delete()
    return redirect("kennel")

def delete_service(request, pk):
    service = Service.objects.get(pk=pk)
    service.delete()
    return redirect("service")

def delete_img(request, pk):
    image = Galery.objects.get(pk=pk)
    image.delete()
    return redirect("service")

def contact(request):
    return render(request, "contact.html", {})