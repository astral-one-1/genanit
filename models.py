from django.db import models

class Location(models.Model):
    id = models.AutoField(primary_key=True)  # Avtomatik ID
    address = models.CharField(max_length=255)  # Manzil
    name = models.CharField(max_length=100)  # Nomi
    details = models.TextField(blank=True, null=True)  # Tavsilot
    image = models.CharField(max_length=100)  # Hajmi (maydon yoki hajm birligida)
    audio = models.FileField(upload_to='audio/')

    def __str__(self):
        return f"{self.name} - {self.address}"


class acounds(models.Model):
    name  = models.CharField(max_length=123)
    login = models.CharField(max_length=123)
    password = models.CharField(max_length=123)

    def __str__(self):
        return "{}-{}".format(self.login, self.password)


# AI Kubra uchun

class Kubra(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
   

    def __str__(self):
        return "{}-{}".format(self.name, self.description)
    