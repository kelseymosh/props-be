from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=250, null=True)
    profile_img = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.username


class Plant(models.Model):
    name = models.CharField(max_length=100, null=True)
    img = models.CharField(max_length=250, null=True)
    wishlist = models.CharField(max_length=250, null=True)
    description = models.CharField(max_length=500, null=True)
    users = models.ManyToManyField(User, related_name='users', through='Favorite')

    def __str__(self):
        return f'{self.id}: {self.name}'


class Favorite(models.Model):
    plant = models.ForeignKey(Plant, blank=True, null=True, related_name='favorite', on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, related_name='favorite', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'