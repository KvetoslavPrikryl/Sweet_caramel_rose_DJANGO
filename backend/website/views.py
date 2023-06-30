from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from .models import User, Dog, Service, Galery
from .form import DogForm, ServiceForm 
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
    trimrovani = []
    for image in galery:
        if image.service == "Trimrování":
            trimrovani.append(image)
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
        "trimrovani" : trimrovani,
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