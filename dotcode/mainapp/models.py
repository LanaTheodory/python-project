from typing import Text
from django.core.checks import messages
from django.db import models
from logapp import models
from logapp.models import *


class Message(models.Model) :
    message = models.TextField()
    sender = models.ForeignKey(User, related_name="message_sender", on_delete=models.CASCADE )
    receiver = models.ForeignKey(User, related_name="message_receiver", on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = BlogManager()
    def __str__(self):
        return self.Text

class Post(models.Model) :
    post = models.TextField()
    user_post = models.ForeignKey(User, related_name="post_user", on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = BlogManager()
    def __str__(self):
        return self.Text

class Comment(models.Model) :
    Text = models.TextField()
    post = models.ForeignKey(Post, related_name="comment_post", on_delete=models.CASCADE) 
    user_comment = models.ForeignKey(User, related_name="comment_user", on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = BlogManager()
    def __str__(self):
        return self.Text


class Reply(models.Model) :
    Text = models.TextField()
    comment = models.ForeignKey(Comment, related_name="reply_comment", on_delete=models.CASCADE) #we can change the related name if its not clear
    user_reply = models.ForeignKey(User, related_name="reply_user", on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = BlogManager()
    def __str__(self):
        return self.Text

class Problem(models.Model) :
    problem = models.TextField()
    user_problem = models.ForeignKey(User, related_name="problem_user", on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # objects = BlogManager()
    def __str__(self):
        return self.Text




def createcomment(postData,user,post):
    return Comment.objects.create(Text=postData['comment2'],post=Post.objects.get(id = post), user_comment = User.objects.get(id = user))
    
    
def createpost(postData,user):
    post=Post.objects.create(post=postData['post'],user_post=User.objects.get(id=user))
    return post


def createmessage(postData,user):#ask  about reply that mean (msg to msg ) 
    msg=Message.objects.create(message=postData['massage'], user_message=User.objects.get(id=user))
    return msg
    
def createproblem(postData,user):
    return Problem.objects.create(problem = postData['problem'] , user_problem = User.objects.get(id=user))

def allproblems():
    return Problem.objects.all()

def get_freelancers():
    
    x = Role.objects.all()
    
    return x
def all_users():

    return User.objects.all()

