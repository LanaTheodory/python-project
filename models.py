from django.db import models
from django.db.models.base import Model
from django.shortcuts import render
from django.db import models
import bcrypt
import re



# class BlogManager(models.Manager):
#     def basic_validator(self, postData ):
#         errors = {}
#         EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
#         if not EMAIL_REGEX.match(postData['email']):    
#             errors['Email'] = "Invalid email address!"
#         unique=User.objects.filter(Email=postData['email']).exists()
#         if(unique):
#             errors['unique'] = "Email exist!"
#         if len(postData['fname']) < 2:
#             errors["fname"] = "first name should be at least 2 characters"
#         if len(postData['lname']) < 2:
#             errors["lname"] = "last name should be at least 2 characters"
#         if len(postData['passwd']) < 8:
#             errors["passwd"] = "your password should be at least 8 characters"
#         return errors
#     def login_validator(self, postdata):
#         errors = {}
#         EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
#         if not EMAIL_REGEX.match(postdata['Email']):    
#             errors['Email'] = "Invalid email address!"
#         if len(postdata['passwd']) < 8:
#             errors["passwd"] = "your password should be at least 8 characters"
#         return errors
#     def thoughts_validator(self, data):
#         errors = {}
#         if len(data['description']) < 8:
#             errors["description"] = "your description should be at least 8 characters"
#         return errors



class Role(models.Model) :
    role = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)




class User(models.Model) :
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    description = models.TextField()
    language = models.CharField(max_length=50)
    skill_level = models.CharField(max_length=50)
    education = models.TextField()
    gender = models.CharField(max_length=10) #shoud we include it?!
    role = models.ForeignKey(Role, related_name="user", on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = BlogManager()

class Message(models.Model) :
    message = models.TextField()
    user_message = models.ForeignKey(User, related_name="message_user", on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = BlogManager()

class Post(models.Model) :
    post = models.TextField()
    user_post = models.ForeignKey(User, related_name="post_user", on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = BlogManager()

class Comment(models.Model) :
    comment = models.TextField()
    post = models.ForeignKey(Post, related_name="comment_post", on_delete=models.CASCADE) #we can change the related name if its not clear
    user_comment = models.ForeignKey(User, related_name="comment_user", on_delete=models.CASCADE )
    reply = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = BlogManager()

