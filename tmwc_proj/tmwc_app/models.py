from django.db import models
import re
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2 or len(postData['first_name']) > 50:
            errors["first_name"] = "First Name must be between 2 and 50 characters long"

        if len(postData['last_name']) < 2 or len(postData['last_name']) > 50:
            errors["last_name"] = "Last Name must be between 2 and 50 characters long"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):              
            errors['email'] = "Invalid email address!"

        if len(postData['password']) < 8:
            errors["password"] = "Password must be at least 8 characters long"

        if postData['password'] != postData['confirmPassword']:
            errors["confirmPassword"] = "Password and Confirm Password do not match"            
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()