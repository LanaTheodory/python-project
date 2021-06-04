from django.db import models
from django.db.models.base import Model
from django.shortcuts import render
from django.db import models
import re
from django.contrib import messages



class BlogManager(models.Manager):
    def basic_validator(self, postData ):
        errors = {}
        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
        if not EMAIL_REGEX.match(postData['email']):    
            errors['email'] = "Invalid email address!"
        unique=User.objects.filter(email=postData['email']).exists()
        if(unique):
            errors['unique'] = "Email exist!"
        if len(postData['first']) < 2:
            errors["first"] = "first name should be at least 2 characters"
        if len(postData['last']) < 2:
            errors["last"] = "last name should be at least 2 characters"
        if len(postData['password-signup']) < 8:
            errors["password"] = "your password should be at least 8 characters"
        return errors
    def login_validator(self, post):
        errors = {}
        EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
        if not EMAIL_REGEX.match(post['email']):    
            errors['email'] = "Invalid email address!"
        if len(post['password_signin']) < 8:
            errors["password"] = "your password should be at least 8 characters"
        return errors
    def lancer_validator(self, data):
        errors = {}
        if len(data['desc']) < 8:
            errors["desc"] = "your description should be at least 8 characters"
        return errors



class Role(models.Model) :
    role = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)




class User(models.Model) :
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=10) 
    # description = models.TextField()
    # language = models.CharField(max_length=50)
    # education = models.TextField()
    role = models.ForeignKey(Role, related_name="user", on_delete=models.CASCADE )
    # lancer_info= models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = BlogManager()


class Lancer_info(models.Model) :
    language = models.CharField(max_length=50)
    education = models.TextField()
    description = models.TextField()
    lancer = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = BlogManager()



def createuser(postData,password):
    # if postData["role"] == "client":
    role = Role.objects.create(role = postData['role'])
    user=User.objects.create(first_name=postData["first"], last_name=postData["last"],
    email=postData["email"], password=password, gender=postData["gender"], role=role)
    return user
    
    # user=User.objects.create(first_name=postData["first"],
    # last_name=postData["last"],email=postData["email"],
    # password=password,gender=postData["gender"],description=postData["desc"],
    # education=postData["edu"],language=postData["lan"],role=role)
    
    # return user

def lancer_info(postData, user_id):

    lancer = Lancer_info.objects.create(description=postData["desc"], 
    education=postData["edu"],language=postData["lan"], lancer = User.objects.get(id= user_id))
    return lancer

# def thislancer(id):
#     return Lancer_info.objects.get(id=id)


def log(email):
    user=User.objects.filter(email=email)
    if user:
        return user[0]
    else:
        return None


