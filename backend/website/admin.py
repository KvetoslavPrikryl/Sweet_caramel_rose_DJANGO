from django.contrib import admin
from .models import User, Service, Galery, Dog,Link

class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "image", "id")

class DogAdmin(admin.ModelAdmin):
    list_display = ("name", "color", "weight", "height", "patel", "body", "dog_sex", "image1", "image2", "image3")
    
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

class GaleryAdmin(admin.ModelAdmin):
    list_display= ("image", "text", "service")

class LinkAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "text")

admin.site.register(User, UserAdmin)
admin.site.register(Dog, DogAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Galery, GaleryAdmin)
admin.site.register(Link, LinkAdmin)
