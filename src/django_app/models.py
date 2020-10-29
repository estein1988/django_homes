from django.db import models

# Create your models here.
class Home(models.Model):
    photo = models.CharField(max_length=100)
    price = models.CharField(max_length=15)
    bed = models.IntegerField()
    bath = models.IntegerField()
    street = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=15)
    lat_long = models.JSONField(default=dict)

    def __str__(self):
        return f'{self.id}: {self.street}'

class Profile(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    social_level = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}: {self.name}'