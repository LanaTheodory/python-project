from django.shortcuts import render, redirect
import bcrypt
from .models import User
from django.contrib import messages


def index(request):
    return render(request, "main.html")


def create_user(request):
    if request.method == 'POST':
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(
        password.encode(), bcrypt.gensalt()).decode()
    pass


def login(request):
    pass