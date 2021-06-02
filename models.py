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



class Client(models.Model) :
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    question = models.TextField()
    gender = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = BlogManager()

class Freelancer(models.Model) :
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    description = models.TextField()
    language = models.CharField(max_length=50)
    skill_level = models.CharField(max_length=50)
    education = models.TextField()
    gender = models.CharField(max_length=10) #shoud we include it?!
    client = models.ManyToManyField(Client, related_name='deals_with') # joint table 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = BlogManager()

class Message(models.Model) :
    message = models.TextField()
    client = models.ForeignKey(Client, related_name="client_message", on_delete=models.CASCADE )
    freelancer = models.ForeignKey(Freelancer, related_name="freelancer_message", on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = BlogManager()

class Post(models.Model) :
    post = models.TextField()
    client = models.ForeignKey(Client, related_name="client_post", on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = BlogManager()

class Comment(models.Model) :
    comment = models.TextField()
    post = models.ForeignKey(Post, related_name="comment_which_post", on_delete=models.CASCADE) #we can change the related name if its not clear
    client = models.ForeignKey(Client, related_name="comment_which_client", on_delete=models.CASCADE, null= True) #the comment is for this client OR this freelancer
    freelancer = models.ForeignKey(Freelancer, related_name="comment_which_freelancer", on_delete=models.CASCADE, null= True) #do we add the freelancer here? 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = BlogManager()

class Reply(models.Model) :
    reply = models.TextField()
    comment = models.ForeignKey(Comment, related_name="reply_which_comment", on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name="reply_which_client", on_delete=models.CASCADE) #the reply is for this client OR this freelancer
    freelancer = models.ForeignKey(Freelancer, related_name="reply_which_freelancer", on_delete=models.CASCADE) #do we add the freelancer here? 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = BlogManager()
