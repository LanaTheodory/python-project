from django.db import models
from django.db.models.expressions import Value
from django.shortcuts import render, redirect
import bcrypt
from .models import *
from django.contrib import messages


def index(request):
    return render(request, "index.html")


def create_user(request):
    if request.method == 'POST':
        password = request.POST['password-signup']
        pw_hash = bcrypt.hashpw(
        password.encode(), bcrypt.gensalt()).decode()
        errors=User.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.item():
                messages.error(request,value)
                return redirect("/log")
        if request.POST['password-signup']!=request.POST["password-signup-conform"]:
            return redirect("/log")
        else:
            request.session['email']=request.POST['email']
            user=create_user(request.POST,password)
            request.session["user_id"]=user.id
        return redirect("/main")


def login(request):
    if request.method == 'POST':
        email = request.POST['Email']
        user =log(email)
        if bcrypt.checkpw(request.POST['password_signin'].encode(), user.password.encode()):
            if user is not None:
                print(user)
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                return redirect('/main')
    return redirect('/log')

    
    

