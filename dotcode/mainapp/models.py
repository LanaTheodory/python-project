from typing import Text
from django.core.checks import messages
from django.db import models
from logapp.models import *


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
    Text = models.TextField()
    post = models.ForeignKey(Post, related_name="comment_post", on_delete=models.CASCADE) #we can change the related name if its not clear
    user_comment = models.ForeignKey(User, related_name="comment_user", on_delete=models.CASCADE )
    reply = models.IntegerField(null=True)# note
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = BlogManager()


def create_comment(postData,user,post):
    Comment.objects.create(Text=postData['text'],post=post,user_comment=user)
    pass
    
def create_post(postData,user):
    post=Post.objects.create(post=postData['post'],user_post=User.objects.get(id=user))
    return post


def create_message(postData,user):#ask  about reply that mean (msg to msg ) 
    msg=Message.objects.create(message=postData['massage'], user_message=User.objects.get(id=user))
    return msg
    