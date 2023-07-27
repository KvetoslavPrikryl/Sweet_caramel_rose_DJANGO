from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.name} {self.body} {self.image}"
    
class Dog(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=50)
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    patel = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    dog_sex = models.CharField(null=True, max_length=6)
    image1 = models.ImageField(null=True, blank=True, upload_to="images/")
    image2 = models.ImageField(null=True, blank=True, upload_to="images/")
    image3 = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.name} {self.color} {self.weight} {self.height} {self.patel} {self.body} {self.dog_sex} {self.image1} {self.image2} {self.image3}"
    
class Service(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(null=True, blank=True)

class Galery(models.Model):
    image = models.ImageField(upload_to="galery/")
    text = models.CharField(max_length=200)
    service = models.CharField(max_length=20)

class Link(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)

