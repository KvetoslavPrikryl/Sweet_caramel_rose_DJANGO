from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logout", views.logout_user, name="logout"),
    path("chovatelska_stanice", views.kennel, name="kennel"),
    path("chovatelska_stanice/<str:pk>", views.dog, name="update"),
    path("delete_dog/<str:pk>", views.delete_dog, name="delete-dog"),
    path("sluzby", views.service, name="service"),
    path("delete_service/<str:pk>", views.delete_service, name="delete-service"),
    path("galerie", views.galery, name="gallery"),
    path("gallery/<str:pk>", views.delete_img, name="delete-img"),
    path("kontakt", views.contact, name="contact"),
    path("odkazy", views.links, name="links"),
    path("odkazy/<str:pk>",views. delete_link, name="delete-link"),
    path("profil/<str:pk>", views.edit_user, name="edit-user")
]