from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData["fn"]) < 2:
            errors["fn"] = "First name should be at least 2 characters"
        if len(postData["ln"]) < 2:
            errors["ln"] = "Last name should be at least 2 characters"
        if len(postData["em"]) < 2:
            errors["em"] = "Email should be at least 5 characters"
        if len(postData["pa"]) < 2:
            errors["pa"] = "Password should be at least 5 characters"
        if postData["pa"] != postData['cp']:
            errors["cp"] = "Pasword doesn't mutch"
        return errors

    def process_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData["mail_e"]) < 2:
            errors["mail_e"] = "Email should be at least 5 characters"
        if len(postData["pass_word"]) < 2:
            errors["pass_word"] = "Password should be at least 5 characters"
        return errors

    def process_add_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData["s_tit"]) < 3:
            errors["s_tit"] = "Title name should be at least 3 characters"
        if len(postData["s_des"]) < 3:
            errors["s_des"] = "Destination should be at least 3 characters"
        if len(postData["s_loc"]) < 3:
            errors["s_loc"] = "Location should be at least 3 characters"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Job(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 
    def __repr__(self):
        return f"Job: {self.name}"

