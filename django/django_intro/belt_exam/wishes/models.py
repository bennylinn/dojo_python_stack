from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.CharField(max_length=85)
    # email_hash ?
    password = models.CharField(max_length=85)

class Wish(models.Model):
    item = models.CharField(max_length=45)
    desc = models.CharField(max_length=300)
    createdTime = models.DateTimeField(auto_now_add=True)

class GrantedWish(models.Model):
    item = models.CharField(max_length=45)
    dateAdded = models.DateTimeField(auto_now=True)
    grantedAt = models.DateTimeField(auto_now_add=True)
    # likes = models.ManyToManyField(User, related_name='likes')
    # user = models.ForeignKey(User, models.CASCADE, related_name="granted_wishes")