from django.db import models
from django.db.models.expressions import Value
from django.shortcuts import render, redirect
import bcrypt
from .models import *
from django.contrib import messages


def index(request):
    if "user_id" in request.session:
        return redirect('/main/community')
    return render(request, "index.html")


def create_user(request):
    if request.method == 'POST':
        
        password = request.POST['password-signup']
        
        pw_hash = bcrypt.hashpw(
        password.encode(), bcrypt.gensalt()).decode()
        errors= User.objects.basic_validator(request.POST)
        if len(errors)>0:
    
            for key,value in errors.items():
                messages.error(request,value)
                return redirect("/log")
        if request.POST['password-signup']!=request.POST["password-signup-conform"]:
        
            return redirect("/log")
        else:
  
            request.session['email']=request.POST['email']
            user= createuser(request.POST,pw_hash)
            request.session["user_id"]=user.id
            request.session['first'] = user.first_name
            request.session['last'] = user.last_name 
            if request.POST['role'] == 'client':
               
                return redirect('/main/community')
        
        return redirect("/log/lancer_reg")
    return redirect("/log")
    

def lancer_reg(request):
    context={
        "all_lan":Language.objects.all()
    }

    return render(request, "login-reg.html",context)


def info(request):
    if request.method == 'POST':
        # lan_id=request.POST.getlist("lan_id[]")
        errors= User.objects.lancer_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request,value)
                return redirect("/log/lancer_reg")
        else:
            user = request.session['user_id']
            lancer= lancer_info(request.POST, user)
            
        return redirect("/main/freelancer_profile/" + str(user))



def login(request) :

    errors = User.objects.login_validator(request.POST)
    
    
    if len(errors):
       
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/log')
    else:
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password_signin']
            user= log(email)
            
            if user :
                request.session['user_id'] = user.id
                request.session['first'] = user.first_name
                request.session['last'] = user.last_name 
                return redirect('/main/community')
        return redirect('/log')




def logout(request):
    request.session.clear()
    return redirect("/log")

    
    

