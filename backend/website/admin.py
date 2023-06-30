from django.contrib import admin
from .models import User, Dog, Service, Galery

class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "image")

class DogAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "body", "dog_sex", "image1", "image2", "image3")

class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

class GaleryAdmin(admin.ModelAdmin):
    list_display= ("image", "text", "service")

admin.site.register(User, UserAdmin)
admin.site.register(Dog, DogAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Galery, GaleryAdmin)
