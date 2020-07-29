from django.db import models
import re

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address."
        if len(postData['first_name']) < 1:
            errors["first_name"] = "First name should be at least 1 character."
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Last name should be at least 1 character."
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['confirm_password'] != postData['password']:
            errors["confirm_password"] = "Please match your passwords."
        return errors
    
    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address."
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        return errors
    
    def edit_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address."
        if len(postData['first_name']) < 1:
            errors["first_name"] = "First name should be at least 1 character."
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Last name should be at least 1 character."
        return errors


class QuotesManager(models.Manager):
    def quote_validator(self, postData):
        errors = {}
        if len(postData['author']) < 4:
            errors["author"] = "Author should be at least 3 characters."
        if len(postData['quote']) < 11:
            errors["quote"] = "Quote should be at least 10 character."
        return errors

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)
    objects = UserManager()
    # Quotes = set of quotes the user can post on the database

class Quotes(models.Model):
    entry = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='quotes', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="likes")
    objects = QuotesManager()

