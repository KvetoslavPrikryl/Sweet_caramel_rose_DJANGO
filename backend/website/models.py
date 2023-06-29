from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.name} {self.body} {self.image}"
