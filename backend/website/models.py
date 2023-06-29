from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.name} {self.body} {self.image}"
    
class Dog(models.Model):
    name = models.CharField(max_length=20)
    link = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    dog_sex = models.CharField(null=True, max_length=6)
    image1 = models.ImageField(null=True, blank=True, upload_to="images/")
    image2 = models.ImageField(null=True, blank=True, upload_to="images/")
    image3 = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.name} {self.link} {self.body} {self.dog_sex} {self.image1} {self.image2} {self.image3}"
    
class Service(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(null=True, blank=True)


