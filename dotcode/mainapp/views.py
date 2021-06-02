from django.shortcuts import render

# Create your views here.
def wallfeed(request):
    return render(request,"wallfeed.html")

def comminty(request):
    return render(request,"comminty.html")

def cliant_profile(request,i):
    pass

def freelancer_profile(request,i):
    pass


def create_comment(request):
    pass

def create_post(request):
    pass


def create_messages(request):
    pass