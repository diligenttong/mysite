from django.db import models


# Create your models here.

class UserInFo(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, null=True)
    age = models.IntegerField(null=True)
    profession = models.CharField(max_length=100,  null=True)
    hobby = models.CharField(max_length=100,  null=True)
    phone = models.CharField(max_length=11, null=True)
    weiChat = models.CharField(max_length=100,  null=True)
    skills = models.CharField(max_length=100, null=True)
    photo = models.ImageField(null=True, upload_to='account/')

    def __str__(self):
        return self.username
