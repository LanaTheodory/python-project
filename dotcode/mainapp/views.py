from django.shortcuts import redirect, render
from .models import *
from logapp import views

def wallfeed(request):
    return render(request,"wallfeed.html")

def community(request):
    user = request.session["user_id"]
    context = {
        'users' : get_user(user),
        'all_problems': allproblems(),
        "all_roles": get_freelancers(),
        'all_users' : all_users(),
    }
    return render(request,"community.html", context )

# def client_profile(request,i):
#     pass

def freelancer_profile(request,i):

    context = {
        'lancer' : thislancer(i),
    }
    
    return render(request, 'freelancer-page2.html', context)


# def create_comment(request):
#     pass

# def create_post(request):
#     pass


# def create_messages(request):
#     pass

def create_problem(request):
    user = request.session["user_id"]

    problem = createproblem(request.POST, user)

    return redirect('/main/community')


