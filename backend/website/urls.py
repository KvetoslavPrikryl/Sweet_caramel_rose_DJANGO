from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logout", views.logout_user, name="logout"),
    path("chovatelska_stanice", views.kennel, name="kennel"),
    path("sluzby", views.service, name="service"),
    path("chovatelska_stanice/<str:pk>", views.dog, name="update"),
    path("delete_dog/<str:pk>", views.delete_dog, name="delete-dog"),
    path("delete_service/<str:pk>", views.delete_service, name="delete-service"),
    path("galerie", views.galery, name="galery"),
]