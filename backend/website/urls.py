from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logout", views.logout_user, name="logout"),
    path("chovatelska_stanice", views.kennel, name="kennel"),
    path("sluzby", views.service, name="service"),
    path("chovatelska_stanice/<str:pk>", views.dog, name="update"),
]