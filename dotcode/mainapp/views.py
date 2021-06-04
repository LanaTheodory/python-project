from django.shortcuts import render
from .models import *

# def wallfeed(request):
#     return render(request,"wallfeed.html")

def community(request):
    return render(request,"community.html")

# def client_profile(request,i):
#     pass

def freelancer_profile(request,i):

    context = {
        # 'lancer' : thislancer(i),
    }
    
    return render(request, 'freelancer-page2.html', context)


# def create_comment(request):
#     pass

# def create_post(request):
#     pass


# def create_messages(request):
#     pass