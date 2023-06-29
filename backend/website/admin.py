from django.contrib import admin
from .models import User, Dog

class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "image")

class DogAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "body", "image1", "image2", "image3")

admin.site.register(User, UserAdmin)
admin.site.register(Dog, DogAdmin)
